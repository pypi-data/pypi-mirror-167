"""Manage bioinformatics pipelines.

Import the package::

   import lnbfx

This is the complete API reference:

.. autosummary::
   :toctree: .

   BfxRun
   schema
   datasets
   dev
"""

__version__ = "0.3.2"

from . import datasets, dev, schema
from ._core import BfxRun, get_bfx_files_from_dir, parse_bfx_file_type  # noqa
