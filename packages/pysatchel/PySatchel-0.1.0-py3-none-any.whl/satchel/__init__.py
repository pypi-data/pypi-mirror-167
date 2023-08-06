from importlib.metadata import version

__version__ = version("pysatchel")

from .aggregate import groupapply
from .iterable import chunk
