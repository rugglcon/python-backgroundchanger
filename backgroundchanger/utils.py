import json
import logging
import platform
import subprocess
import shutil
from tkinter import Tk
from . import config

def reload_gala():
    """
    this only is necessary for systems using the Gala
    WM, notably elementary OS

    this is just a workaround until this issue (https://github.com/elementary/gala/issues/13)
    gets fixed
    """
    subprocess.Popen(['gala', '-r'],
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL)

def get_keys():
    """
    returns a tuple of the two keys
    if there is no secrety key, it will just return None for that
    """
    with open(config.CONFIG_FILE) as key_file:
        data = json.loads(key_file.read())
    if 'secret_key' not in data:
        return {
            'access_key': data['access_key'],
            'secret_key': None
        }
    return data

def change_background(photo_name: str):
    """
    changes the background using a command
    determined by operating system
    """
    cmd = get_background_cmd(photo_name)
    subprocess.call(cmd)

def get_screen_size():
    """
    gets the screen size as a dict
    {height, width}
    """
    root = Tk()
    return {
        'height': root.winfo_vrootheight(),
        'width': root.winfo_vrootwidth()
    }

def copy_file(src, dst):
    logging.info('Copying pic {} to {}'.format(src, dst))
    shutil.copy2(src, dst)

def get_background_cmd(photo_name: str):
    system = platform.system()
    if system == 'Darwin':
        raise ValueError('macOS is not yet implemented to change the background. However, you can still change the background. photo name: {}'.format(photo_name))
    elif system == 'Linux':
        logging.info('Linux OS found; finding distro')
        dist = platform.linux_distribution()
        logging.info('Found {}'.format(dist))
        if 'elementary' in dist or 'Ubuntu' in dist:
            return [
                'gsettings',
                'set',
                'org.gnome.desktop.background',
                'picture-uri',
                'file://' + photo_name
            ]
    elif system == 'Windows':
        raise ValueError('Windows is not yet implemented to change the background. However, you can still change the background. photo name: {}'.format(photo_name))
    raise ValueError('{} is not yet implemented to change the background. However, you can still change the background. photo name: {}'.format(system, photo_name))