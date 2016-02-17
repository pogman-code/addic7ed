from os import makedirs
from os.path import expanduser, exists

from logging import getLogger, Formatter, StreamHandler, DEBUG, WARN
from logging.handlers import RotatingFileHandler

from termcolor import colored


LOG_COLORS = {
    'DEBUG': 'grey',
    'INFO': 'cyan',
    'WARNING': 'yellow',
    'ERROR': 'magenta',
    'CRITICAL': 'red'
}


def init_logger():
    logger = getLogger('addic7ed')
    logger.setLevel(DEBUG)

    directory = expanduser('~') + '/.config/addic7ed/'
    if not exists(directory):
        makedirs(directory)

    fh = RotatingFileHandler(directory + "addic7ed.log")
    fh.setLevel(DEBUG)

    sh = StreamHandler()
    sh.setLevel(WARN)

    fcolor = colored("%(asctime)s", 'green') + " - %(levelname)8s - %(name)s - %(message)s"
    formatter_color = ColoredFormatter(fcolor)
    formatter = Formatter("%(asctime)s - %(levelname)8s - %(name)s - %(message)s");
    fh.setFormatter(formatter)
    sh.setFormatter(formatter_color)
    logger.addHandler(fh)
    logger.addHandler(sh)


class ColoredFormatter(Formatter):
    def format(self, record):
        levelname = record.levelname
        record.msg = colored(record.msg, LOG_COLORS[levelname])
        msg = Formatter.format(self, record)
        return msg
