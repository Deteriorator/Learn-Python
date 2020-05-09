#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    peopleinteract_update.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   9:38
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

import shelve
from person import Person

fieldnames = ('name', 'age', 'job', 'pay')

db = shelve.open('class-shelve')
while True:
    key = input('\nkey? => ')
    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
        for field in fieldnames:
            currval = getattr(record, field)
            newnext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
            if newnext:
                setattr(record, field, eval(newnext))
    db[key] = record
db.close()

