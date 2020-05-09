#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    dump_db_classes.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   9:10
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print(bob.last_name())
print(db['tom'].last_name())

