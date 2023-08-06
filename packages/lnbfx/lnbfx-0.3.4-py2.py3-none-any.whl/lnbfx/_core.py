from pathlib import Path
from typing import Union

from lnschema_core import id
from sqlmodel import Session, select  # noqa
from sqlmodel.sql.expression import Select, SelectOfScalar

import lnbfx.schema as schema  # noqa

from .dev import parse_bfx_file_type

# avoid SAWarning from sqlalchemy
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


class BfxRun:
    def __init__(self, *, pipeline: dict, run_id: str = None):
        self._pipeline_id = pipeline["id"]
        self._pipeline_v = pipeline["v"]
        self._pipeline_name = pipeline["name"]
        self._pipeline_reference = pipeline["reference"]
        if run_id is None:
            self._run_id = id.pipeline_run()
        else:
            self._run_id = run_id
        self._ingested = False
        self._run_dir = None
        self._db_engine = None

    @property
    def pipeline_id(self):
        """Pipeline id."""
        return self._pipeline_id

    @property
    def pipeline_v(self):
        """Pipeline version."""
        return self._pipeline_v

    @property
    def pipeline_name(self):
        """Pipeline name."""
        return self._pipeline_name

    @property
    def pipeline_reference(self):
        """Pipeline reference."""
        return self._pipeline_reference

    @property
    def run_id(self):
        """Pipeline run id."""
        return self._run_id

    @property
    def run_name(self):
        """Pipeline run name."""
        return self.run_dir

    @property
    def run_dir(self):
        """BFX pipeline run dir."""
        return self._run_dir

    @run_dir.setter
    def run_dir(self, dirpath):
        if isinstance(dirpath, str):
            dirpath = Path(dirpath)
        self._run_dir = dirpath

    @property
    def db_engine(self):
        """Database engine."""
        return self._db_engine

    @db_engine.setter
    def db_engine(self, engine):
        self._db_engine = engine

    def get_pipeline_pk(self):
        """Queries pipeline and returns private key.

        Args:
            None.

        Returns:
            Tuple with the pipeline id and version.

        Raises:
            RuntimeError: If the pipeline has not been ingested yet.
        """
        pipeline = self._query_bfx_pipeline()
        if pipeline is None:
            raise RuntimeError(
                "Unable to get pipeline private key. Pipeline not yet ingested."
            )
        return (pipeline.id, pipeline.v)

    def get_run_pk(self) -> str:
        """Queries pipeline run and returns private key.

        Args:
            None.

        Returns:
            str: Pipeline run id.

        Raises:
            RuntimeError: If the pipeline run has not been ingested yet.
        """
        pipeline_run = self._query_bfx_run()
        if pipeline_run is None:
            raise RuntimeError(
                "Unable to get pipeline run private key. Pipeline run not yet ingested."
            )
        return pipeline_run.id

    def check_and_ingest(self):
        """Ingests bionformatics pipeline and pipeline run if that hasn't been done yet.

        Args:
            pipeline_run_id: An a primary key id for the
            `lnschema_core.pipeline_run` table.

        Returns:
            None.
        """
        # check if pipeline and run entries exist in the database
        pipeline = self._query_bfx_pipeline()
        run = self._query_bfx_run()
        # insert missing entries
        if pipeline is None:
            pipeline = self._insert_bfx_pipeline()
        if run is None:
            run = self._insert_bfx_run(pipeline.id, pipeline.v)

    def link_dobject(self, dobject_id: str, dobject_filepath: Union[str, Path]):
        """Ingest bfxmeta and add link between dobject and bfx file type.

        Args:
            dobject_id (str): dobject's ID.
            dobject_filepath (Union[str, Path]): dobject's filepath.

        Returns:
            None.
        """
        # parse dobject file type according to its position in the file system
        if self._run_dir is not None and str(self._run_dir) in str(
            Path(dobject_filepath)
        ):
            file_type = parse_bfx_file_type(dobject_filepath, from_dir=True)
        else:
            file_type = parse_bfx_file_type(dobject_filepath, from_dir=False)
        dobject_dirpath = str(Path(dobject_filepath).parent.resolve())
        bfxmeta_id = self._insert_bfxmeta(file_type, dobject_dirpath).id
        self._insert_dobject_bfxmeta(dobject_id, bfxmeta_id)

    def _insert_bfx_run(self, bfx_pipeline_id: str, bfx_pipeline_v: str):
        """Inserts entry in the bfx_run table."""
        with Session(self._db_engine) as session:
            bfx_run_entry = schema.bfx_run(
                id=self._run_id,
                dir=str(self.run_dir),
                bfx_pipeline_id=bfx_pipeline_id,
                bfx_pipeline_v=bfx_pipeline_v,
            )
            session.add(bfx_run_entry)
            session.commit()
            session.refresh(bfx_run_entry)
            return bfx_run_entry

    def _insert_bfx_pipeline(self):
        """Inserts entry in the bfx_pipeline table."""
        with Session(self._db_engine) as session:
            bfx_pipeline_entry = schema.bfx_pipeline(
                id=self._pipeline_id,
                v=self._pipeline_v,
            )
            session.add(bfx_pipeline_entry)
            session.commit()
            session.refresh(bfx_pipeline_entry)
            return bfx_pipeline_entry

    def _insert_bfxmeta(self, file_type: str, dirpath: str):
        """Inserts entry in the bfxmeta table."""
        with Session(self._db_engine) as session:
            bfxmeta_entry = session.exec(
                select(schema.bfxmeta).where(
                    schema.bfxmeta.file_type == file_type,
                    schema.bfxmeta.dir == dirpath,
                )
            ).first()
            if bfxmeta_entry is None:
                bfxmeta_entry = schema.bfxmeta(file_type=file_type, dir=dirpath)
                session.add(bfxmeta_entry)
                session.commit()
                session.refresh(bfxmeta_entry)
            return bfxmeta_entry

    def _insert_dobject_bfxmeta(self, dobject_id: str, bfxmeta_id: int):
        """Inserts entry in the dobject_bfxmeta table."""
        dobject_bfxmeta_entry = schema.dobject_bfxmeta(
            dobject_id=dobject_id, bfxmeta_id=bfxmeta_id
        )
        with Session(self._db_engine) as session:
            session.add(dobject_bfxmeta_entry)
            session.commit()
            session.refresh(dobject_bfxmeta_entry)
        return dobject_bfxmeta_entry

    def _query_bfx_pipeline(self):
        """Queries bfx pipeline."""
        with Session(self._db_engine) as session:
            bfx_pipeline_entry = session.exec(
                select(schema.bfx_pipeline).where(
                    schema.bfx_pipeline.id == self._pipeline_id,
                    schema.bfx_pipeline.v == self._pipeline_v,
                )
            ).first()
        return bfx_pipeline_entry

    def _query_bfx_run(self):
        """Queries bfx pipeline run."""
        with Session(self._db_engine) as session:
            bfx_run_entry = session.exec(
                select(schema.bfx_run).where(
                    schema.bfx_run.id == self._run_id,
                )
            ).first()
        return bfx_run_entry
