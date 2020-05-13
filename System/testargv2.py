#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    testargv2.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.09   17:51
-------------------------------------------------------------------------------
   @Change:   2020.05.09
-------------------------------------------------------------------------------
"""

def get_opts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv
    myargs = get_opts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)


