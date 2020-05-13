#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    moreplus.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.13   9:49
-------------------------------------------------------------------------------
   @Change:   2020.05.13
-------------------------------------------------------------------------------
"""

import sys


def getrepley():
    if sys.stdin.isatty():
        return input('? ')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getche()
            msvcrt.putch(b'\n')
            return key
        else:
            assert False, 'Platform not supported'


def more(text, numlines=10):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getrepley() not in ['y', 'Y', b'y', b'Y']: break


if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1], 'r', encoding='UTF-8').read())

