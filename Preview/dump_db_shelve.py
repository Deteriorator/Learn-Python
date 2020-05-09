#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    dump_db_shelve.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   17:25
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()

