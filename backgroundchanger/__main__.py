from . import config
from . import api
from . import utils

def main():
    keys = utils.get_keys()
    api_object = api.Api(keys[0], keys[1])
    photo = api_object.get_random()
    utils.change_background(photo)

main()