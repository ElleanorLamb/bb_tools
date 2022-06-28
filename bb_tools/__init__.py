__version__ = "v0.0.1"

from .bassetti_erskine import *

from pathlib import Path
_pkg_root = Path(__file__).parent.absolute()
del(Path)
