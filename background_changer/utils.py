import json
import platform
import subprocess
from tkinter import Tk
from . import config

def get_keys():
    """
    returns a tuple of the two keys
    if there is no secrety key, it will just return None for that
    """
    with open(config.CONFIG_FILE) as key_file:
        data = json.loads(key_file.read())
    if 'secret_key' not in data:
        return (data['access_key'], None)
    else:
        return (data['access_key'], data['secret_key'])

def change_background(photo_name: str):
    """
    changes the background using a command
    determined by operating system
    """
    cmd = get_background_cmd(photo_name)
    subprocess.call(cmd)

def get_screen_size():
    """
    gets the screen size as a tuple
    (height, width)
    """
    root = Tk()
    return (root.winfo_height(), root.winfo_width())

def get_background_cmd(photo_name: str):
    system = platform.system()
    if system == 'Darwin':
        raise ValueError('macOS is not yet implemented to change the background. However, you can still change the background. photo name: {}'.format(photo_name))
    elif system == 'Linux':
        dist = platform.linux_distribution()
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