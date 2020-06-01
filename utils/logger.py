# coding: utf8

import os
import logging
from logging.handlers import RotatingFileHandler
# from concurrent_log_handler import ConcurrentRotatingFileHandler

from logging import StreamHandler

# region colorprint 支持
_colors = {
    'black': 30, 'red': 31,
    'green': 32, 'yellow': 33,
    'blue': 34, 'magenta': 35,
    'cyan': 36, 'white': 37,
}

_backgrounds = {
    'black': 40, 'red': 41,
    'green': 42, 'yellow': 43,
    'blue': 44, 'magenta': 45,
    'cyan': 46, 'white': 47,
}

_formats = {
    'default': 2, 'bold': 1,
    'dark': 2, 'underline': 4,
    'blink': 5, 'reverse': 7,
    'concealed': 8,
}


# grey,red, green,yellow,blue,magenta,cyan,white
def colorprint(content, color='white', bgcolor='black', str_format='default'):
    content = '\033[' \
              + str(_formats.get(str_format, '0')) \
              + ';' + str(_colors.get(color, '47')) \
              + ';' + str(_backgrounds.get(bgcolor, '40')) \
              + 'm' + str(content) + ' \033[0m'

    print(content)


def cprint(content, color='cyan', str_format='default', end='\n'):
    """暂时不考虑bg的颜色"""
    content = '\033[' \
              + str(_formats.get(str_format, '0')) \
              + ';' + str(_colors.get(color, '47')) \
              + 'm' + str(content) + ' \033[0m'
    print(content, end=end)


# endregion


fmt = "%(levelname)s %(filename)s line: %(lineno)d %(asctime)s :%(message)s"
data_fmt = "%a %d %b %Y %H:%M:%S"


def set_logger(name, level_='DEBUG', filter_=None, formatter_=None, filename=None):
    if not filter_:
        filter_ = logging.Filter()

    if not formatter_:
        formatter_ = logging.Formatter(fmt, data_fmt)

    if not filename:
        filename = os.path.join(os.path.abspath(__file__), '..', 'logs', 'default.logs')

    file_dir = os.path.dirname(filename)
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)

    handle_ = (RotatingFileHandler(filename=filename, maxBytes=1024 * 1024 * 30, backupCount=10, encoding='utf8'),
               # handle_ = (ConcurrentRotatingFileHandler(filename=filename, maxBytes=1024 * 1024 * 3, backupCount=10, encoding='utf8'),
               # StreamHandler()  # 同步输出到终端
               )

    _logger = logging.getLogger(name)
    for hd in handle_:
        hd.setFormatter(formatter_)
        hd.addFilter(filter_)
        hd.setLevel(level_)
        _logger.addHandler(hd)
    _logger.setLevel(level_)
    return _logger


# 日志级别, DEBUG, INFO, WARN, ERROR, CRITICAL
log = set_logger(name='default', level_='DEBUG',
                 filename=os.path.join(os.path.dirname(__file__), 'logs', 'corsair_client.log'))
