#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    reader.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.12   9:00
-------------------------------------------------------------------------------
   @Change:   2020.05.12
-------------------------------------------------------------------------------
"""

print('Got this: "%s"' % input())
import sys
data = sys.stdin.readline()[:-1]
print('The meaning if life is ', data, int(data) * 2)


