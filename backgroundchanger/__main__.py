import pywal
from . import config
from . import api
from . import utils

def do_wal(photo):
    img = pywal.image.get(photo)
    colors = pywal.colors.get(img)
    pywal.sequences.send(colors)
    pywal.export.every(colors)
    pywal.wallpaper.change(img)

def main():
    keys = utils.get_keys()
    api_object = api.Api(keys)
    photo = api_object.get_random()
    # utils.change_background(photo)
    do_wal(photo)

if __name__ == '__main__':
    main()