#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    lister_recur.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.15   9:52
-------------------------------------------------------------------------------
   @Change:   2020.05.15
-------------------------------------------------------------------------------
"""

import sys
import os


def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):
        path = os.path.join(currdir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)


if __name__ == '__main__':
    mylister(sys.argv[1])



