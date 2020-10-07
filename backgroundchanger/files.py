from os import path, mkdir


class FolderNotCreatedException(Exception):
    def __init__(self, message):
        super(FolderNotCreatedException, self).__init__(message)


def _create_folder(folder):
  if not path.exists(folder):
      try:
          mkdir(folder)
      except OSError:
        msg = f'Not was possible to create folder %s' % folder
        raise FolderNotCreatedException(msg)


def create_folders(folder_paths):
  for folder_path in folder_paths:
    _create_folder(folder_path)


def file_not_exists(file):
  return not path.exists(file)
  
