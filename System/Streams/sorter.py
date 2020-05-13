#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    sorter.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.12   9:03
-------------------------------------------------------------------------------
   @Change:   2020.05.12
-------------------------------------------------------------------------------
"""

import sys
lines = sys.stdin.readlines()
lines.sort()
for line in lines:
    print(line, end='')

