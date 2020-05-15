#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    lister_walk.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.15   9:44
-------------------------------------------------------------------------------
   @Change:   2020.05.15
-------------------------------------------------------------------------------
"""

import sys
import os


def lister(root):
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('[' + thisdir + ']')
        for fname in fileshere:
            path = os.path.join(thisdir, fname)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])

