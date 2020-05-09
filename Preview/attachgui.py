#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    attachgui.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   17:04
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

from tkinter import *
from tkinter102 import MyGui

mainwin = Tk()
Label(mainwin, text=__name__).pack()


popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()


