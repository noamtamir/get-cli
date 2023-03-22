import os
from pathlib import Path

DEFAULT_EDITOR = os.getenv('EDITOR', 'vim')
DEFAULT_STORAGE_PATH = Path.home() / '.get.yml'
DEFAULT_STORAGE_DATA = {'hello': 'world'}
