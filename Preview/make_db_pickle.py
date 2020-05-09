#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    make_db_pickle.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   14:24
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

from initdata import db
import pickle

dbfile = open('people-file', 'wb')
pickle.dump(db, dbfile)
dbfile.close()

