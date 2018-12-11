import setuptools

try:
    import backgroundchanger
except ImportError:
    print("background_changer requires python 3.5 or greater. Exiting.")
    quit(1)

with open('README.md', 'r') as ld:
    long_desc = ld.read()

setuptools.setup(
        name='backgroundchanger',
        version=backgroundchanger.config.VERSION,
        author=backgroundchanger.config.AUTHOR,
        author_email=backgroundchanger.config.EMAIL,
        description='background changer using unsplash API.',
        long_description=long_desc,
        license='MIT',
        url=backgroundchanger.config.URL,
        python_requires='>=3.5',
        zip_safe=False,
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License'
        ]
)
