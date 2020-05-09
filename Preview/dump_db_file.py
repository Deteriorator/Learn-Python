#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    dump_db_file.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   14:08
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

from make_db_file import load_dbase

db = load_dbase()
for key in db:
    print(key, '=>\n  ', db[key])

print(db['sue']['name'])
