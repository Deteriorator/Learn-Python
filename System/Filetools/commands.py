#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    commands.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.14   17:59
-------------------------------------------------------------------------------
   @Change:   2020.05.14
-------------------------------------------------------------------------------
"""

from sys import argv
from scanfile import scanner


class UnknownCommand(Exception):
    pass


# def process_line(line):
#     if line[0] == '*':
#         print("Ms.", line[1:-1])
#     elif line[0] == '+':
#         print('Mr.', line[1:-1])
#     else:
#         raise UnknownCommand(line)

"""
上面的方法是前一段代码
"""
commands = {'*': 'Ms.', '+': 'Mr.'}


def process_line(line):
    try:
        print(commands[line[0]], line[1:-1])
    except:
        raise UnknownCommand(line)


filename = 'data.txt'
if len(argv) == 2:
    filename = argv[1]
    scanner(filename, process_line)
