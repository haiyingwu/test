#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/18
# @Author  : halliewu
# @File    : decorate.py
import time


def timeit(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used:', end - start

    return wrapper

@timeit
def foo():
    print 'in foo()'

foo()