import logging
from os import path
import requests
from . import config
from . import utils

class Api():
    """
    class to work with the API
    """

    def __init__(self, keys):
        self.__api_route__ = 'https://api.unsplash.com'
        self.access_key = keys['access_key']
        self.secret_key = keys['secret_key']
        self.version_header = {'Accept-Version': 'v1'}

    def get_random(self):
        """
        gets a random photo

        returns the full path to the downloaded photo
        """
        # gets the url for the main request
        url = self.__api_route__ + '/photos/random?client_id={}'.format(self.access_key)
        res = self.request('GET', url, headers=self.version_header).json()

        # we need the screen size for getting the correct image size
        screen_size = utils.get_screen_size()
        logging.debug('got the screen size: {}'.format(screen_size))
        # construct the new url params
        download_params = '&h={}&w={}&fm={}&fit=crop'.format(screen_size['height'], screen_size['width'], config.IMG_FORMAT)
        bg_name = path.join(config.CONFIG_DOWNLOAD_FOLDER, res['id'] + '.' + config.IMG_FORMAT)
        self.download_photo(str(res['urls']['raw']) + download_params, bg_name)
        utils.copy_file(bg_name, path.join(config.BACKGROUNDS_LOCAL, res['id'] + '.' + config.IMG_FORMAT))
        logging.debug('downloaded photo to {}'.format(bg_name))
        return bg_name

    def request(self, method: str, url: str, data=None, headers=None):
        """
        generic request method

        returns the result of the request
        """
        res = requests.request(method=method, url=url, data=data, headers=headers)
        if res.status_code == 200:
            return res
        else:
            raise Exception('something went wrong with your request')

    def download_photo(self, download_url: str, name: str):
        """
        downloads a photo and saves it to disk
        """
        with open(name, 'wb') as file:
            res = self.request('GET', download_url, headers=self.version_header)
            file.write(res.content)