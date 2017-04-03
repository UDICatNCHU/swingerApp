from distutils.core import setup

setup(
    name = 'swingerApp',
    packages = ['swingerApp'],
    version = '1.0',
    description = 'django app of swinger',
    author = 'davidtnfsh',
    author_email = 'davidtnfsh@gmail.com',
    url = 'https://github.com/UDICatNCHU/swingerApp',
    download_url = 'https://github.com/UDICatNCHU/swingerApp/archive/v1.0.tar.gz',
    keywords = ['swinger',],
    classifiers = [],
    license='GPL3.0',
    install_requires=[
        'Swinger'
    ],
    zip_safe=True
)
