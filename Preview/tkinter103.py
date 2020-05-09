#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    tkinter103.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   17:18
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='Hello %s' % name)


top = Tk()
top.title('Echo')
# top.iconbitmap('py-blue-trans-out.ico')

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text="Submit", command=(lambda : reply(ent.get())))
btn.pack(side=LEFT)
top.mainloop()
