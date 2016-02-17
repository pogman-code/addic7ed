import logging

from os.path import expanduser
from configparser import ConfigParser
from .constants import LANG_ISO, LANG_DEFAULT, CONFIG_FILE_NAME


class Config(object):
    __instance = None

    _lang = None

    _config_file = ConfigParser()

    def __new__(cls):
        if Config.__instance is None:
            Config.__instance = object.__new__(cls)
        return Config.__instance

    def __init__(self):
        self.logger = logging.getLogger('addic7ed.Config')
        self._config_file.read(expanduser("~") + "/" + CONFIG_FILE_NAME)

    def set_lang(self, lang):
        if lang in LANG_ISO.keys():
            self._lang = LANG_ISO[lang]
            self.logger.info("Language {0} is now set.".format(self._lang['lang']))
        else:
            self.logger.warn("{0} is not a valid language code.".format(lang))

    def get_lang(self):
        if self._lang and "addic7ed" in self._config_file and "lang" in self._config_file["addic7ed"]:
            self.set_lang(self._config_file["addic7ed"]["lang"])
        if self._lang is None:
            self.set_lang(LANG_DEFAULT)
        return self._lang

    def get_lang_code(self):
        return self.get_lang()["code"]

    def get_lang_name(self):
        return self.get_lang()['lang']
