import logging
import argparse

from sys import exit
from operator import getitem
from os.path import expanduser
from configparser import ConfigParser

from .constants import LANG_ISO, LANG_DEFAULT, CONFIG_FILE_NAME


def singleton(cls):
    instance = cls()

    def __call__():
        return instance

    return instance


@singleton
class Config():
    _lang = None

    _config_file = ConfigParser()

    def __init__(self):
        self.logger = logging.getLogger('addic7ed.Config')
        self.args = None
        self._config_file.read(expanduser("~") + "/" + CONFIG_FILE_NAME)

    def set_lang(self, lang):
        if lang in LANG_ISO.keys():
            self._lang = LANG_ISO[lang]
            self.logger.info("Language %s is now set." % (self._lang['lang']))
        else:
            self.logger.warn("%s is not a valid language code." % lang)

    def get_lang(self):
        if self._lang and "addic7ed" in self._config_file and "lang" in self._config_file["addic7ed"]:
            self.logger.info("Set language %s from config file" % self._config_file["addic7ed"]["lang"])
            self.set_lang(self._config_file["addic7ed"]["lang"])
        if self._lang is None:
            self.logger.info("Set default language : %s" % LANG_DEFAULT)
            self.set_lang(LANG_DEFAULT)
        return self._lang

    def get_lang_code(self):
        return self.get_lang()["code"]

    def get_lang_name(self):
        return self.get_lang()['lang']

    def get_args(self):
        return self.args

    def get_arg(self, arg):
        return self.args[arg]

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Download subtitles for TV Shows from addic7ed site.')

        parser.add_argument('-l', '--lang', type=valid_lang,
                            help='language used to search subtitles.')

        parser.add_argument('--list-lang', action='store_true', help='list languages supported.')

        self.args = parser.parse_args()

        if self.args.list_lang:
            self.print_languages_list()
            exit(0)

        if self.args.lang:
            self.set_lang(self.args.lang)

    def print_languages_list(self):
        for x in sorted(LANG_ISO.items(), key=lambda x: getitem(x[1], 'lang')):
            print("{0:<20}\t\t{1}".format(x[1]['lang'], x[0]))


def valid_lang(lang):
    if lang not in LANG_ISO.keys():
        msg = "%s is not a valid language code." % lang
        raise argparse.ArgumentTypeError(msg)
    return lang
