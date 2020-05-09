#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    manager.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   17:42
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""

from person import Person


class Manager(Person):
    def give_raise(self, percent, bonus=0.1):
        # self.pay *= (1.0 + percent + bonus)
        Person.give_raise(self, percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)
    print(tom)
