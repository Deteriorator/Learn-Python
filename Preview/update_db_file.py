#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    update_db_file.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   14:10
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

from make_db_file import load_dbase, store_dbase

db = load_dbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

store_dbase(db)

