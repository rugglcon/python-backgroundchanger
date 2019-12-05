import argparse
import logging
from os import path, mkdir
from sys import exit
import pywal
from . import config
from . import api
from . import utils

def setup():
    """
    sets up logging, initial info, and arg parsing
    returns parsed args
    """
    logging.basicConfig(filename=config.LOGFILE, level=logging.DEBUG)
    if not path.exists(config.CONFIG_FOLDER):
        mkdir(config.CONFIG_FOLDER)
    if not path.exists(config.CONFIG_FILE):
        logging.critical('Config file {} not found'.format(config.CONFIG_FILE))
        raise FileNotFoundError('Config file {} not found. This is needed to get the access key for unsplash'.format(config.CONFIG_FILE))
    if not path.exists(config.CONFIG_DOWNLOAD_FOLDER):
        mkdir(config.CONFIG_DOWNLOAD_FOLDER)

    args = argparse.ArgumentParser()
    args.add_argument('-n', action='store_false',
        help='Don\'t generate a colorscheme or set terminal colors')
    args.add_argument('-v', action='store_true',
        help='Print version')
    return args.parse_args()

def do_wal(photo, do_colors=True):
    """
    takes care of everything 'wal'
    """
    img = pywal.image.get(photo)
    if do_colors:
        colors = pywal.colors.get(img)
        pywal.sequences.send(colors, sequences=True)
        pywal.export.every(colors)
    pywal.wallpaper.change(img)
    utils.change_background(img)
    utils.reload_gala()

def main():
    parsed = setup()

    if parsed.v:
        print('backgroundchanger v{}'.format(config.VERSION))
        exit(0)

    set_colors = parsed.n
    logging.debug('Should set pywal colors: {}'.format(set_colors))

    keys = utils.get_keys()
    logging.debug('Got the keys: {}'.format(keys))
    api_object = api.Api(keys)
    photo = api_object.get_random()
    do_wal(photo, set_colors)

if __name__ == '__main__':
    main()