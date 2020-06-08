#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    fork1.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.20   9:13
-------------------------------------------------------------------------------
   @Change:   2020.05.20
-------------------------------------------------------------------------------
"""

import os


def child():
    print('Hello from child', os.getpgid())
    os._exit(0)


def parent():
    while True:
        newpid = os.fork()   # windows 上无法进行操作
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break


parent()

