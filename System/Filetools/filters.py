#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    filters.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.15   9:05
-------------------------------------------------------------------------------
   @Change:   2020.05.15
-------------------------------------------------------------------------------
"""

import sys


def filter_files(name, function):
    input = open(name, 'r')
    output = open(name + '.out', 'w')
    for line in input:
        output.write(function(line))
    input.close()
    output.close()


def filter_stream(funtion):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(funtion(line), end='')


if __name__ == '__main__':
    filter_stream(lambda line: line)
