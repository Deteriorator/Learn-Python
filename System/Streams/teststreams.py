#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    teststreams.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.11   19:12
-------------------------------------------------------------------------------
   @Change:   2020.05.11
-------------------------------------------------------------------------------
"""

def interact():
    print('Hello stream world')
    while True:
        try:
            reply = input('Enter a number> ')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()

