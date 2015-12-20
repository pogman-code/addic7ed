# Addic7ed Scraper
**First of all, be aware that this is a VERY FIRST draft of a scraper for Addic7ed.com's subtitles**

## Requirements
This scraper is made to work with Python 3 only.
It is pre-installed on many linux distribution.

If it's not your case, install it :p

## Install

    git clone https://github.com/Jesus-21/addic7ed.git addic7ed
    cd addic7ed

then

    sudo pip install -r requirements.txt
or use python [Python virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and install requirements within.

Finally, edit *constants.py* file to uncomment the language you need.

## Usage
*addic7ed.py* file should be excutable, just run it from the folder where your video files are.

    $ /git/clone/path/addic7ed.py

then it will prompt which file you want to download.
If download is successful, it will rename the video file to match subtitle file.

## TODO List

 - Colored output
 - Packaging (for pip/easy_install)
 - Error management (almost none right now)
 - Langue choice through config file
 - Intelligent auto-download (using release name + completion + popularity)
 - Better file crawling (recursivity mainly)
 - More pre/post processing of series names
 - (Python 2 support?)

Suggestions and/or pull requests are more than welcome!
