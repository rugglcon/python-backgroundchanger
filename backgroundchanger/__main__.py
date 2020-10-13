import argparse
import logging
from sys import exit
import pywal
import json
import distro
from backgroundchanger.files import create_folders, file_not_exists
from . import config
from . import api
from . import utils


def start_log():
    logging.basicConfig(filename=config.LOGFILE, level=logging.DEBUG)


def create_config_folders():
    setup_folders = [config.CONFIG_FOLDER, config.CONFIG_DOWNLOAD_FOLDER]
    create_folders(setup_folders)


def create_config_file(key=None):
    if key:
        data = key
        with open(config.CONFIG_FILE, 'w') as key_file:
            json.dump(obj=data, fp=key_file, indent=4)

    if file_not_exists(config.CONFIG_FILE):
        msg = 'File {} not found. This is needed to get the access key for unsplash.\n'.format(config.CONFIG_FILE)
        msg += 'Please provide the access key.'
        raise FileNotFoundError(msg)


def parse_arguments():
    args = argparse.ArgumentParser()

    args.add_argument('-n', action='store_false',
                      help='Don\'t generate a colorscheme or set terminal colors')

    args.add_argument('-v', action='store_true',
                      help='Print version')

    key_group = args.add_argument_group('key_group')

    key_group.add_argument('-a', '--access',
                           help='Provide the Unsplash API access key.')

    key_group.add_argument('-s', '--secret',
                           help='Provide the Unsplash API secret key')

    return args.parse_args()


def do_wal(photo, do_colors=True):
    """
    takes care of everything 'wal'
    """
    img = pywal.image.get(photo)
    if do_colors:
        colors = pywal.colors.get(img)
        pywal.sequences.send(colors)
        pywal.export.every(colors)
    pywal.wallpaper.change(img)
    utils.change_background(img)
    if 'elementary' in distro.name():
        utils.reload_gala()


def main():
    keys = {}
    parsed = parse_arguments()
    if parsed.access:
        keys['access_key'] = parsed.access
    if parsed.secret:
        keys['secret_key'] = parsed.secret

    try:
        start_log()
        create_config_folders()
        create_config_file(key=keys)
    except Exception as error:
        logging.exception(error)
        raise error

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
