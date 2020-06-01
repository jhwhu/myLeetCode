# coding: utf8
# @Author       : danny.jiang
# @time         : 2019-09-05 17:19
# @File         : jd_decrotor.py
# @Software     : PyCharm

import traceback
from functools import wraps
import sys

from utils.logger import log

if str(sys.version_info.major) + '.' + str(sys.version_info.minor) >= '3.7':
    OrderedDict = dict
else:
    from collections import OrderedDict

tag_saver = {}
x = globals()


class StopIfFailException(Exception):
    def __str__(self):
        return "Force Stopped"


def stop_if_fail(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            result, info = func(*args, **kwargs)
            if result == False:
                raise StopIfFailException
        except:
            raise StopIfFailException

    return inner


def catch_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except StopIfFailException:
            raise StopIfFailException
        except:
            traceback.print_exc()
            return False, str("JD_FRAMEWORK_EXCEPTION: " + traceback.format_exc())

    return inner

# def write_keyword_result(func, reporter, *args, **kwargs):
#     result = func(*args, **kwargs)
#     if len(result) <= 2:
#         log.error("interface返回结果必须是len=2的列表类型 (True, 'doc')")
#         result = False, str(result)
#     result_bool = 'PASS' if result[0] == True else 'FAIL'
#     reporter.startKeyword(name=func.__name__, doc=result[1], status=result_bool)
#     reporter.endKeyword(name=func.__name__, doc=result[1], status=result_bool)
