#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    person.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.06   17:38
-------------------------------------------------------------------------------
   @Change:   2020.05.06
-------------------------------------------------------------------------------
"""


class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'Software')
    sue = Person('Sue Jones', 45, 40000, 'Hardware')
    print(bob.name, sue.pay)
    print(bob.last_name())
    sue.give_raise(.10)
    print(sue.pay)
