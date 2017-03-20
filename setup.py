from setuptools import setup, find_packages
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='addic7ed',
    version='1.1.5',

    description=('Addic7ed scraper written in Python '
                 'to download subtitles (almost) automatically'),
    long_description=long_description,
    url='https://github.com/Jesus-21/addic7ed',
    author='Adrian MAURIN',
    author_email='adrian.maurin@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search'
    ],

    keywords='subtitles addic7ed scraper',
    packages=find_packages(exclude=['readme']),

    install_requires=['beautifulsoup4',
                      'fuzzywuzzy',
                      'python-Levenshtein',
                      'requests',
                      'termcolor'],

    entry_points={
        'console_scripts': [
            'addic7ed=addic7ed.__init__:addic7ed',
        ],
    },
)
