#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    more.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.09   9:38
-------------------------------------------------------------------------------
   @Change:   2020.05.09
-------------------------------------------------------------------------------
"""


def more(text, numlines=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More? (y or Y): ') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    # 注释部分是第二章部分的代码
    # import sys
    #
    # more(open(sys.argv[1], 'r', encoding='UTF-8').read(), 10)

    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
