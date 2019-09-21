#!/usr/bin/env python
# encoding: utf-8
"""
@author: wanwei
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: wei_wan
@software: pycharm
@file: batch_convert_encoding.py
@time: 2019/5/28 14:38
@desc:
"""

import os
import sys

in_enc="gb18030"
out_enc="utf-8"


'''
def convert(filename):
    in_enc = globals()['in_enc']
    out_enc = globals()['out_enc']
    with open(filename, 'r', encoding=in_enc,errors='ignore') as f:
        content = f.read()
    with open(filename, 'w', encoding=out_enc) as f1:
        f1.write(content)
    print(filename + "................done")
'''

def convert(filename):
    in_enc = globals()['in_enc']
    out_enc = globals()['out_enc']
    try:
        with open(filename, 'r', encoding=in_enc,errors='ignore') as f:
            content = f.read()
        with open(filename, 'w', encoding=out_enc) as f1:
            f1.write(content)
        print(filename + "................done")
    except IOError as err:
        print("{0}     ERROR:{1}".format(err.args[0], err.args[1]))
    except UnicodeDecodeError as err2:
        print(err2.with_traceback())

def explorer(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            if os.path.isfile(path):
                convert(path)
            if os.path.isdir(path):
                explorer(path)


def judge_file_dir(path):
    if os.path.isfile(path):
        convert(path)
    if os.path.isdir(path):
        explorer(path)


def main():
    for path in sys.argv[1:]:
        path = os.path.join(path)
        judge_file_dir(path)


if __name__ == "__main__":
    sys.argv.append('/Users/mac/Desktop/data_mining/data/sogou_before')
    main()
