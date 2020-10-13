import pytest

from backgroundchanger.files import create_folders, file_not_exists
from os import listdir


@pytest.mark.usefixtures("temp_folder")
def test_create_folders():
    folders = ['./tmp/images', './tmp/background']
    create_folders(folders)

    assert all(x in listdir('./tmp/') for x in ['background', 'images'])


@pytest.mark.usefixtures("temp_folder")
def test_should_raise_an_error_when_try_to_create_invalid_folder():
    create_folders(['./tmp/:'])

    with pytest.raises(Exception) as error:
        assert 'Not was possible to create folder :' == error.message


@pytest.mark.usefixtures("temp_folder")
def test_file_not_exists():
    open("./tmp/text.txt", "+w").close()

    assert file_not_exists('./tmp/text.txt') == False
    assert file_not_exists('./tmp/not_found.txt') == True
