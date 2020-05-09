#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    dump_db_pickle.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   14:26
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

import pickle

dbfile = open('people-file', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n  ', db[key])
print(db['sue']['name'])



