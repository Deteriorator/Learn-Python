#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    update_db_pickle.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   14:29
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

import pickle

dbfile = open('people-file', 'rb')
db = pickle.load(dbfile)
dbfile.close()

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

dbfile = open('people-file', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
