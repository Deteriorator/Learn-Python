#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    fork-exec.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.20   9:25
-------------------------------------------------------------------------------
   @Change:   2020.05.20
-------------------------------------------------------------------------------
"""

import os


parm = 0
while True:
    parm += 1
    # can't run on windows
    pid = os.fork()
    if pid == 0:
        os.execlp('python', 'python', 'child.py', str(parm))
        assert False, 'error starting program'
    else:
        print('Child is ', pid)
        if input() == 'q':
            break


