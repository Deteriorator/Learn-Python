#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    fork-count.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.20   9:18
-------------------------------------------------------------------------------
   @Change:   2020.05.20
-------------------------------------------------------------------------------
"""


import os, time


def counters(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))


for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counters(5)
        os._exit(0)


print('Main Process exiting.')

