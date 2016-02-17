import argparse

from sys import exit
from operator import getitem

from .constants import LANG_ISO
from .config import Config

def parseargs():
    parser = argparse.ArgumentParser(description='Download subtitles for TV Shows from addic7ed website.')

    parser.add_argument('-l', '--lang', type=valid_lang,
                        help='language used to search subtitles.')

    parser.add_argument('--list-lang', action='store_true', help='list languages supported.')

    args = parser.parse_args()

    if args.list_lang:
        print_languages_list()
        exit(0)

    if args.lang:
        Config().set_lang(args.lang)


def valid_lang(lang):
    if lang not in LANG_ISO.keys():
        msg = "{0} is not a valid language code.".format(lang)
        raise argparse.ArgumentTypeError(msg)
    return lang

def print_languages_list():
    for x in sorted(LANG_ISO.items(),key=lambda x:getitem(x[1],'lang')):
        print("{0:<20}\t\t{1}".format(x[1]['lang'],x[0]))
