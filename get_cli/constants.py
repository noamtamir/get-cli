from pathlib import Path

DEFAULT_EDITOR = 'vim'  # TODO: os.getenv('EDITOR', 'vim')
DEFAULT_STORAGE_PATH = Path.home() / '.get.yml'
DEFAULT_STORAGE_DATA = {'hello': 'world'}
