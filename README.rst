
Addic7ed Scraper
================

Requirements
------------

This scraper is made to work with Python 3 only. It is pre-installed on
many linux distribution.

If it's not your case, install it :p

Install
-------

Using python-pip:
    ::

        $ sudo pip install addic7ed

Using Git repository:
    ::

        $ git clone https://github.com/Jesus-21/addic7ed.git addic7ed

    or download/unzip
    `archive <https://github.com/Jesus-21/addic7ed/archive/master.zip>`__

    then (from download/clone path):

    ::

        $ sudo pip install -r requirements.txt

    or use python `Python
    virtualenv <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__
    and install requirements within.

Create ~/.addic7edrc file containing language you want (english for instance):
::

    [addic7ed]
    lang = en

You can find language codes `here <https://github.com/Jesus-21/addic7ed/blob/master/addic7ed/constants.py>`__

Usage
-----

If you installed using python-pip, just run *addic7ed* (otherwise *addic7ed.py* file should be excutable) from the folder where your video files are,
::

    $ addic7ed

or

::

    $ /git/clone/path/addic7ed.py

following command line arguments can be provided:
 ::
    positional arguments:
        PATH                  path of file to search subtitles for (default: all
                                video from current dir).

    optional arguments:
        -h, --help            show this help message and exit
        --list-lang           list supported languages.
        -n, --dry-run         do not ask or download subtitlejust output available
                                ones and leave.
        -l LANG, --lang LANG  language to search subs for (default: en).
        -k, --keep-lang       suffix subtitle file with language code.
        -e EXTENSIONS [EXTENSIONS ...], --extensions EXTENSIONS [EXTENSIONS ...]
                                Find subtitles for files matching given extensions
                                (space separated values)
        --names-from-file NAMES_FROM_FILE
                                read file names from a file.
        --paths-from-file PATHS_FROM_FILE
                                read file paths from a file.
        -r {none,sub,video}, --rename {none,sub,video}
                                rename sub/video to match video/sub or none at all
                                (default: none).

then it will prompt which file you want to download. If download is
successful, it will rename the video file to match subtitle file.

|Example|

TODO List
---------
-  Error management/reporting
-  Intelligent auto-download (using comment + completion +
   popularity)
-  Better file crawling (recursivity mainly)

Suggestions and/or pull requests are more than welcome!

.. |Example| image:: https://raw.githubusercontent.com/Jesus-21/addic7ed/master/readme/capture.jpg
