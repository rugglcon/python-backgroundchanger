import setuptools

try:
    import background_changer
except ImportError:
    print("background_changer requires python 3.5 or greater. Exiting.")
    quit(1)

setuptools.setup(
        name='background_changer',
        version=background_changer.config.VERSION,
        author=background_changer.config.AUTHOR,
        author_email=background_changer.config.EMAIL,
        description='background changer using unsplash API.',
        license='MIT',
        url=background_changer.config.URL,
        packages=['background_changer'],
        python_requires='>=3.5',
        zip_safe=False
)
