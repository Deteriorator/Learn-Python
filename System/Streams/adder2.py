#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    adder2.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.12   9:48
-------------------------------------------------------------------------------
   @Change:   2020.05.12
-------------------------------------------------------------------------------
"""

import sys
sum = 0
while True:
    line = sys.stdin.readline()
    if not line:
        break
    sum += int(line)
print(sum)

