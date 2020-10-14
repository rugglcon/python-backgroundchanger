import platform
import shutil
import subprocess
import unittest
from os import getcwd, makedirs, path, remove
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from backgroundchanger import config, utils
from open_file_mock import MockOpen

class TestExceptions(unittest.TestCase):
    def test_mac_exception(self):
        platform.system = MagicMock(return_value='Darwin')
        self.assertRaises(
            ValueError, utils.get_background_cmd, "./tests/test.png")

    def test_win_exception(self):
        platform.system = MagicMock(return_value='Windows')
        self.assertRaises(
            ValueError, utils.get_background_cmd, "./tests/test.png")

    def test_linux_cmd(self):
        platform.system = MagicMock(return_value='Linux')
        platform.linux_distribution = MagicMock(return_value='Ubuntu')
        res = utils.get_background_cmd("./tests/test.png")
        assert res[0] == 'gsettings'


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


@patch('backgroundchanger.utils.subprocess.Popen')
def test_reload_gala(mock_popen):
    utils.reload_gala()
    mock_popen.assert_called_once_with(['gala', '-r'],
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL)


def test_copy_file():
    destDir = './tests/dummyDest/'
    srcDir = './tests/dummySrc/'
    if not path.exists(destDir):
        makedirs(destDir)
    if not path.exists(srcDir):
        makedirs(srcDir)
    with open(path.join(getcwd(), 'tests/', 'dummySrc/' 'dummy.txt'), 'w+') as fp:
        pass
    utils.copy_file('./tests/dummySrc/dummy.txt', './tests/dummyDest/')
    assert path.isfile('./tests/dummyDest/dummy.txt')
    shutil.rmtree(destDir)
    shutil.rmtree(srcDir)


def test_get_background_cmd():
    t = TestExceptions()
    t.test_mac_exception()
    t.test_win_exception()
    t.test_linux_cmd()


@patch('backgroundchanger.utils.subprocess.call')
def test_change_background(mock_call):
    utils.get_background_cmd = MagicMock()
    utils.get_background_cmd.return_value = ['dummy','cmd']
    utils.change_background("./tests/test.png")
    mock_call.assert_called_once_with(['dummy', 'cmd'])
