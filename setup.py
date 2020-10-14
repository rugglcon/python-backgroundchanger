import setuptools

# get package details from backgroundchanger/config.py
from backgroundchanger import config

with open('README.md', 'r') as ld:
    long_desc = ld.read()

setuptools.setup(
        name='backgroundchanger',
        version=config.VERSION,
        author=config.AUTHOR,
        author_email=config.EMAIL,
        description='background changer using unsplash API.',
        long_description=long_desc,
        long_description_content_type="text/markdown",
        license='MIT',
        url=config.URL,
        python_requires='>=3.5',
        zip_safe=False,
        entry_points={
            'console_scripts': [
                'backgroundchanger=backgroundchanger.__main__:main'
            ]
        },
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License'
        ],
        install_requires=[
            'requests >=2.0, <3.0',
            'pywal >=3.0, <4.0',
            'distro >=1.0, <2.0'
        ]
)
