#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    tkinter102.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.07   9:59
-------------------------------------------------------------------------------
   @Change:   2020.05.07
-------------------------------------------------------------------------------
"""

from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()

