import setuptools

try:
    import backgroundchanger
except ImportError:
    print("background_changer requires python 3.5 or greater. Exiting.")
    quit(1)

setuptools.setup(
        name='backgroundchanger',
        version=backgroundchanger.config.VERSION,
        author=backgroundchanger.config.AUTHOR,
        author_email=backgroundchanger.config.EMAIL,
        description='background changer using unsplash API.',
        license='MIT',
        url=backgroundchanger.config.URL,
        packages=['background_changer'],
        python_requires='>=3.5',
        zip_safe=False
)
