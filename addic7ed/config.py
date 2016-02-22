import logging
from os.path import expanduser

from argparse import ArgumentParser, ArgumentTypeError
from configparser import ConfigParser

from .constants import LANG_ISO, LANG_DEFAULT, CONFIG_FILE_NAME

logger = logging.getLogger("addic7ed.config")
DEFAULT = {
    "lang": LANG_DEFAULT,
    "rename": "none"
}


def singleton(cls):
    instance = cls()

    def __call__():
        return instance

    return instance


def _valid_lang(lang):
    if lang not in LANG_ISO.keys():
        msg = "%s is not a valid language code." % lang
        raise ArgumentTypeError(msg)
    return lang


def _lang_list():
    llist = "%25s %s" % ("NAME", "CODE")
    for x in sorted(LANG_ISO.items(), key=lambda x: x[1]["name"]):
        llist = "%s\n%25s %s" % (llist, x[1]["name"], x[0])
    return llist


@singleton
class Config():
    def __init__(self):
        for k, v in DEFAULT.items():
            setattr(self, k, v)

    def load(self):
        self._from_file()
        self._from_args()

    def _from_file(self):
        logger.info("Loading config from file")
        config_file = ConfigParser()
        config_file.read("%s/%s" % (expanduser("~"), CONFIG_FILE_NAME))
        if "addic7ed" in config_file:
            for k, v in config_file["addic7ed"].items():
                if k in DEFAULT:
                    logger.info("Setting '%s' from config file: %s" % (k, v))
                    setattr(self, k, v)
                else:
                    logger.warn("Unknown key '%s' in config file" % k)

    def _from_args(self):
        logger.info("Loading config from CLI args")
        parser = ArgumentParser(description=(
            "Addic7ed scraper to download subtitles (almost) automatically"
        ))

        parser.add_argument("--list-lang", action="store_true",
                            help="list supported languages.")
        parser.add_argument("-l", "--lang", type=_valid_lang,
                            help="language to search subs for (default: en).")
        parser.add_argument("-r", "--rename",
                            choices=["none", "sub", "video"],
                            help=("TBD. rename sub/video to match video/sub "
                                  "or none at all (default: none)."))

        args = parser.parse_args()

        if args.list_lang:
            print(_lang_list())
            exit(0)

        if args.lang:
            logger.info("Setting 'lang' from config file: %s" % args.lang)
            self.lang = args.lang

    def __setattr__(self, name, value):
        if name == "lang":
            if value in LANG_ISO.keys():
                logger.info("Language '%s' is now set." % value)
                super().__setattr__("_%s" % name, value)
            else:
                logger.warn("%s is not a valid language code, using %s" %
                            (value, self._lang))
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == "lang":
            return LANG_ISO[self._lang]
        else:
            return super().__getattr__(name)
