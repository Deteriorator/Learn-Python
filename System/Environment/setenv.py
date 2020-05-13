#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    setenv.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.11   9:40
-------------------------------------------------------------------------------
   @Change:   2020.05.11
-------------------------------------------------------------------------------
"""

import os

print('Setenv...', end=' ')
print(os.environ['USERNAME'])

os.environ['USERNAME'] = 'Brian'
os.system('python echoenv.py')

os.environ['USERNAME'] = 'Arthur'
os.system('python echoenv.py')

os.environ['USERNAME'] = input('?')
print(os.popen('python echoenv.py').read())

