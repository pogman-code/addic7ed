import logging
from os.path import expanduser, exists

from argparse import ArgumentParser, ArgumentTypeError, FileType
from configparser import ConfigParser

from .constants import LANG_ISO, LANG_DEFAULT, CONFIG_FILE_NAME

logger = logging.getLogger("addic7ed.config")
RENAME_MODES = ("none", "sub", "video")
DEFAULT = {
    "lang": LANG_DEFAULT,
    "rename": "none",
    "keep_lang": False,
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

        parser.add_argument("paths", metavar="PATH", type=str, nargs='*',
                            help=("path of file to search subtitles for ("
                                  "default: all video from current dir)."))
        parser.add_argument("--list-lang", action="store_true",
                            help="list supported languages.")
        parser.add_argument("-n", "--dry-run", action="store_true",
                            help=("do not ask or download subtitle"
                                  "just output available ones and leave."))
        parser.add_argument("-l", "--lang", type=_valid_lang,
                            help="language to search subs for (default: en).")
        parser.add_argument("-k", "--keep-lang", action="store_true",
                            help="suffix subtitle file with language code.")
        parser.add_argument("-f", "--from-file", type=FileType('r'),
                            help="read files paths from a file.")
        parser.add_argument("-r", "--rename",
                            choices=RENAME_MODES,
                            help=("rename sub/video to match video/sub "
                                  "or none at all (default: none)."))

        args = parser.parse_args()

        if args.list_lang:
            print(_lang_list())
            exit(0)

        self.dry_run = args.dry_run
        self.paths = [p for p in args.paths if exists(p)]

        if args.lang:
            logger.info("Setting 'lang' from config file: %s" % args.lang)
            self.lang = args.lang

        if args.from_file:
            files = sorted(args.from_file.read().splitlines())
            self.paths.extend([f for f in files if exists(f)])

        if args.keep_lang:
            self.keep_lang = args.keep_lang

        if args.rename:
            self.rename = args.rename

    def __setattr__(self, name, value):
        if name == "lang":
            if value in LANG_ISO.keys():
                logger.info("Language '%s' is now set." % value)
                super().__setattr__(name, dict({"iso": value},
                                               **LANG_ISO[value]))
            else:
                logger.warn("%s is not a valid language code, using %s" %
                            (value, self.lang["iso"]))
        elif name == "keep_lang":
            super().__setattr__(name, str(value) == "True")
        elif name == "rename":
            if value in RENAME_MODES:
                logger.info("Rename mode is now set to '%s'." % value)
                super().__setattr__(name, value)
            else:
                logger.warn("%s is not a valid rename mode, using %s" %
                            (value, self.rename))
        else:
            super().__setattr__(name, value)
