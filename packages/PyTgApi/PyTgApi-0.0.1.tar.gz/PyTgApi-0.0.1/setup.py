from distutils.core import setup

setup(
    name = 'PyTgApi',
    packages = ['PyTgApi'],
    version = '0.0.1',
    license = 'GNU General Public License v3.0',
    description = 'A python library for Telegram Bot Api.', 
    author = 'Sasta Dev',
    author_email = 'sastadev2007@gmail.com',
    url = 'https://github.com/SastaDev/PyTgApi',
    download_url = 'https://github.com/SastaDev/PyTgApi/archive/refs/tags/v0.0.1.tar.gz',
    keywords = ['PyTgApi'],
    install_requires = [
        'requests'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)