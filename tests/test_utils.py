import shutil
import subprocess
import unittest
from os import getcwd, makedirs, path, remove
from pathlib import Path
from mock import MagicMock, patch

from backgroundchanger import utils
from open_file_mock import MockOpen

@patch('backgroundchanger.utils.platform_system')
class TestExceptions(unittest.TestCase):
    def test_mac_exception(self, mock_platform):
        mock_platform.return_value = 'Darwin'
        self.assertRaises(
            ValueError, utils.get_background_cmd, "./tests/test.png")


    def test_win_exception(self, mock_platform):
        mock_platform.return_value = 'Windows'
        self.assertRaises(
            ValueError, utils.get_background_cmd, "./tests/test.png")

    @patch('backgroundchanger.utils.distro_name')
    def test_linux_cmd(self, mock_distro, mock_platform):
        mock_distro.return_value = 'Ubuntu'
        mock_platform.return_value = 'Linux'
        res = utils.get_background_cmd("./tests/test.png")
        assert res[0] == 'gsettings'


@patch('backgroundchanger.utils.Tk')
def test_get_screen_size(mock_tk):
    mock_tk.return_value.winfo_vrootheight = MagicMock()
    mock_tk.return_value.winfo_vrootheight.return_value = 10
    mock_tk.return_value.winfo_vrootwidth = MagicMock()
    mock_tk.return_value.winfo_vrootwidth.return_value = 10
    screen = utils.get_screen_size()
    assert screen['height'] == 10
    assert screen['width'] == 10


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


@patch('backgroundchanger.utils.Popen')
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


@patch('backgroundchanger.utils.call')
def test_change_background(mock_call):
    utils.get_background_cmd = MagicMock()
    utils.get_background_cmd.return_value = ['dummy','cmd']
    utils.change_background("./tests/test.png")
    mock_call.assert_called_once_with(['dummy', 'cmd'])
