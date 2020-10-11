# Background Changer
A small program in Python 3 that grabs a random photo from [Unsplash](https://unsplash.com) according to your screen resolution and sets it as your background.

## Further testing

This hasn't yet been tested on Windows or Mac ([being worked on](https://github.com/rugglcon/python-backgroundchanger/issues/1)), but it works for Ubuntu Linux. Any commands I might have gotten wrong to set it as your background, please feel free to fix those or add more!

## Dependencies
This is pretty light on dependencies, but you will need to make sure you have a couple things:

* `tkinter` - a python GUI toolkit, but is only used to get the screen resolution. This is usually installed via a system package.
* `requests` - python module for HTTP requests.
* `pywal` - generates color schemes and used for changing the wallpaper.

## How to contribute?

For issue and PR guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

### Environment setup

**NOTE:** For Mac, first test if you have `tkinter` directly installed with your Python version first:
```sh
python3
>>> import tkinter
```
If that doesn't cause an error, you're good. If it does, follow [this](https://stackoverflow.com/a/60469203/9565946) Stack Overflow
to get that correctly set up. Then you can continue with the rest of the steps.

1. Create a virtual environment and install the dependencies
```sh
### using venv
python -m venv ./venv

source ./venv/bin/activate
###


### using pyenv virtualenv
pyenv virtualenv 3.8.2 backgroundchanger

pyenv local backgroundchanger
###

# install dev requirements
pip install -r requirements-dev.txt -r requirements.txt
```

2. Build the project and install locally
```sh
python setup.py bdist_wheel

pip install -e
```

3. Run the project
```sh
backgroundchanger
```

### Running tests
```sh
pytest tests
```

## Source for images in python3 
Source is built for use in small, low-traffic applications. For production uses, we recommend the official Unsplash API which has more robust features and supports high-traffic use cases.Check out the Unsplash API.


**Random from a specific user**
To choose a random photo from a specific user, the format follows that of selecting from a collection.
Parameters
https://source.unsplash.com/user/{USERNAME}
* Optionally, to specify a size, append it at the end of the base URL.
Example
https://source.unsplash.com/user/erondu/1600x900
HTML Example
<img src="https://source.unsplash.com/user/erondu/1600x900">


**Random from a user’s likes**
Similar to finding a photo taken by a user, you can fetch a random photo that has been liked by a specific user.
Parameters
https://source.unsplash.com/user/{USERNAME}/likes
* Optionally, to specify a size, append it at the end of the base URL.
Example
https://source.unsplash.com/user/jackie/likes/1600x900
HTML Example
<img src="https://source.unsplash.com/user/jackie/likes/1600x900">

**Random from a collection**
You can also select a random photo from a given collection.
Parameters
https://source.unsplash.com/collection/{COLLECTION ID}
* Optionally, to specify a size, append it at the end of the base URL.
Example
https://source.unsplash.com/collection/190727/1600x900
HTML Example
<img src="https://source.unsplash.com/collection/190727/1600x900">


**Fixed daily/weekly photo**
All of the above URL's will give you a new photo each time they are requested (provided there are enough photos to choose from given the filtering). However each can also be limited to only updating once per day or week. To do so, simply append /daily or /weekly to the URL.
https://source.unsplash.com/daily
Random from a user
https://source.unsplash.com/user/erondu/daily
Random from a search term
