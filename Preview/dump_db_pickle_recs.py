#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    dump_db_pickle_recs.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   16:02
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""



import pickle, glob

for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)


suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name'])
