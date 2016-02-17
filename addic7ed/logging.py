from os import makedirs
from os.path import expanduser, exists

from logging import getLogger, Formatter, StreamHandler, DEBUG, WARN
from logging.handlers import RotatingFileHandler


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

    formatter = Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(sh)
