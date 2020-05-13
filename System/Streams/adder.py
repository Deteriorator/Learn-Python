#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    adder.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.12   9:04
-------------------------------------------------------------------------------
   @Change:   2020.05.12
-------------------------------------------------------------------------------
"""

import sys

sum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        sum += int(line)
print(sum)

