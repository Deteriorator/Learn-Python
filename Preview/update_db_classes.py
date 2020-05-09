#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    update_db_classes.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   9:26
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

import shelve

db = shelve.open('class-shelve')

sue = db['sue']
sue.give_raise(.25)
db['sue'] = sue

tom = db['tom']
tom.give_raise(.20)
db['tom'] = tom
db.close()

