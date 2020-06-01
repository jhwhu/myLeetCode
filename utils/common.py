# coding: utf8
# @Author       : danny.jiang
# @time         : 2019-09-03 15:16
# @File         : common.py
# @Software     : PyCharm

import os
import pickle
import sys
import random
import string
import traceback
import socket
import platform
import zipfile
import datetime
from functools import reduce
from contextlib import closing
import pathlib
import hashlib
import yaml
# 不能换成path, path.Path().glob('**/*.py')不是递归的
import pathlib as path


def calc_md5(s: str):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))  # 注意转码
    res = md5.hexdigest()
    return res


def random_str(_len: int):
    """用于支持xw脚本中生成随机字符串"""
    return ''.join([random.choice(string.printable) for _ in range(int(_len))])


def file_must_exist(fl):
    if not os.path.exists(str(fl)):
        raise Exception(f"{fl} 不存在. 请将该文件放到 tester 目录下.")


def read_yaml_data(yaml_loc='', _encoding='utf8'):
    file_must_exist(str(yaml_loc))

    if os.path.exists(str(yaml_loc)) is False:
        sys.stderr(f'yaml file does not exist. location is: {str(yaml_loc)}. \n'
                   f'subprocess will quit.')
        return None

    try:
        with open(str(yaml_loc), "r", encoding=_encoding) as fh:
            fd = fh.read()
    except:
        with open(str(yaml_loc), "r", encoding="gbk") as fh:
            fd = fh.read()

    try:
        yaml_content = yaml.load(fd, yaml.loader.SafeLoader)
    except:
        sys.stderr(f'file_loc: {yaml_loc}')
        sys.stderr(traceback.format_exc())
        sys.stderr('yaml文件格式不正确')
        sys.exit(0)
        # return None
    return yaml_content


def parse_file_location(base, suffix):
    """把后缀为  x.x.x.x 的字符串转意为文件路径, 和base拼接在一起"""
    suffix = suffix.replace(r"\\", "/") \
        .replace("\\", "/") \
        .split('/')
    return reduce(lambda x, y: x / y, [base] + suffix)


def get_host_ip():
    ip = '127.0.0.1'
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        try:
            s.close()
        except:
            pass

    return ip


def isPortOccupied(port, localHostIp=True):
    s = socket.socket()
    s.settimeout(1)
    hostIp = '127.0.0.1' if localHostIp else get_host_ip()

    try:
        return s.connect_ex((hostIp, port)) == 0  # 0 --> 连接成功 --> occupied
    finally:
        s.close()


def isMacOs():
    if 'darwin' in platform.platform().lower():
        return True
    return False


def isWindowsOs():
    if 'windows' in platform.platform().lower():
        return True
    return False


def zipLocalFile(fileLoc, zipedFileName, deleteOriginalFile=False):
    if os.path.exists(fileLoc) is False:
        return False

    z = zipfile.ZipFile(zipedFileName, 'w', zipfile.ZIP_DEFLATED)
    z.write(fileLoc)
    z.close()

    if deleteOriginalFile:
        os.remove(fileLoc)
    return True


def downloadByHttp(url, des):
    import requests
    with closing(requests.get(url, stream=True, verify=False)) as res:
            # for chunk in res.iter_content(chunk_size=1024):
            #     if chunk:
            #         fd.write(chunk)
        with open(des, 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)


    # req = requests.get(url, stream=True)
    # with open(des, 'wb') as f:
    #     for chunk in req.iter_content(chunk_size=1024):
    #         if chunk:
    #             f.write(chunk)


# 把用例文件及修改时间保存到txt文件中
def save_file_Time(folder: path.Path):
    for tc_file in folder.glob("**/*.yaml"):
        fileName = tc_file
        file_modifitime = os.path.getmtime(fileName)
        with open(r"./fileTime.txt", "a") as fw:
            fw.write(','.join(['%s' % fileName, '%s\n' % file_modifitime]))


# 读取文件获取file和修改时间
def get_fileTime_data():
    txt = open('fileTime.txt', 'r').readlines()
    file_time = {}
    for row in txt:
        (key, value) = row.split(',')
        file_time[key] = value
    print(file_time)
    return file_time


# 获取新文件或文件修改时间变更的文件
def get_new_file(folder: path.Path):
    ftdata = get_fileTime_data()
    for tc_file in folder.glob("**/*.yaml"):
        file_modifitime = os.path.getmtime(tc_file)
        if tc_file not in ftdata.keys():
            return tc_file
        elif tc_file in ftdata.keys() and file_modifitime != ftdata[tc_file]:
            return tc_file
        else:
            continue
