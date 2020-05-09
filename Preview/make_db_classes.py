#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    make_db_classes.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   9:04
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'Software')
sue = Person('Sue Jones', 45, 40000, 'Hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

