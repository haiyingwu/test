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

def test(m, n, c=None):
    if m == n:
        print 'ok'
    c_test(n,c)

def c_test(n,c=None):
    if c is None:
        t=5
        print t
    else:
        print 'error'

if __name__ == "__main__":

    test(1, 2)
    print "/Users/hallie/project/test/decorate.py"
