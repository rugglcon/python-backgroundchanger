# Background Changer
A small program in Python 3 that grabs a random photo from [Unsplash](https://unsplash.com) according to your screen resolution and sets it as your background.

## Further testing

This hasn't yet been tested on Windows or Mac, but it works for Ubuntu Linux. Any commands I might have gotten wrong to set it as your background, please feel free to fix those or add more!

## Dependencies
This is pretty light on dependencies, but you will need to make sure you have a couple things:

* `tkinter` - a python GUI toolkit, but is only used to get the screen resolution. This is usually installed via a system package.
* `requests` - python module for HTTP requests. Install with `pip3 install requests`
* `pywal` - generates color schemes and used for changing the wallpaper. Install with `pip3 install pywal`