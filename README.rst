Addic7ed Scraper
================

**First of all, be aware that this is a VERY FIRST draft of a scraper
for Addic7ed.com's subtitles**

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

Finally, edit *constants.py* file to uncomment the language you need.

TBD / NOT YET AVAILABLE!

Create ~/.addic7edrc file containing language you want (english for instance):
::

    [config]
    lang = 1

You can find language codes `here <https://github.com/Jesus-21/addic7ed/blob/master/constants.py>`__

Usage
-----

If you installed using python-pip, just run *addic7ed* (otherwise *addic7ed.py* file should be excutable) from the folder where your video files are,
::

    $ addic7ed

or

::

    $ /git/clone/path/addic7ed.py

then it will prompt which file you want to download. If download is
successful, it will rename the video file to match subtitle file.

|Example|

TODO List
---------
-  Error management (almost none right now)
-  Langue choice through config file
-  Intelligent auto-download (using release name + completion +
   popularity)
-  Better file crawling (recursivity mainly)
-  More pre/post processing of series names
-  (Python 2 support?)

Suggestions and/or pull requests are more than welcome!

.. |Example| image:: https://raw.githubusercontent.com/Jesus-21/addic7ed/master/readme/capture.jpg
