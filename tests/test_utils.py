import pytest
from backgroundchanger import utils
from backgroundchanger import config
from unittest.mock import patch
from open_file_mock import MockOpen
from pathlib import Path
from os import path





def test_get_screen_size():
    screen = utils.get_screen_size()
    assert screen['height']
    assert screen['width']

def test_get_keys():
    with patch('builtins.open', new_callable=MockOpen) as open_mock:
        jsonStr = '''
                {
            "access_key" : "ak",
            "secret_key" : "sk"
        }'''
        config_file_path = path.join(Path.home(), '.config', 'python-backgroundchanger','unsplash_keys.json')
        open_mock.set_read_data_for(path=config_file_path, data=jsonStr)
        keys = utils.get_keys()
        assert keys['access_key'] =='ak'
        assert keys['secret_key'] =='sk'