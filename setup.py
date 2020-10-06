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
        long_description_content_type="text/markdown",
        license='MIT',
        url=backgroundchanger.config.URL,
        python_requires='>=3.5',
        zip_safe=False,
        entry_points={'console_scripts': ['backgroundchanger=backgroundchanger.__main__:main']},
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License'
        ]
)
