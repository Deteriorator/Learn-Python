#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    scanfile.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.14   17:58
-------------------------------------------------------------------------------
   @Change:   2020.05.14
-------------------------------------------------------------------------------
"""

def scanner(name, function):
    file = open(name, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        function(line)
    file.close()

