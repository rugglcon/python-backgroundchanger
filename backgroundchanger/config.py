from pathlib import Path

AUTHOR = 'Connor Ruggles'
EMAIL = 'conruggles@gmail.com'
VERSION = '0.1.0'
URL = 'https://github.com/rugglcon/python-backgroundchanger'
CONFIG_FOLDER = str(Path.joinpath(Path.home(), '.python-backgroundchanger'))
CONFIG_FILE = Path.joinpath(CONFIG_FOLDER, 'unsplash_keys.json')
CONFIG_DOWNLOAD_FOLDER = Path.joinpath(CONFIG_FOLDER, 'photos')