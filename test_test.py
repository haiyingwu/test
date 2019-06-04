#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/21
# @Author  : halliewu
# @File    : test_test.py

def test(m ,n ,c=None,d=None):
    # if m>n:
    #     print 'ok'
    # if m>c:
    #     print 'error'
    if c is None and d is None:
        print "all none"
    elif c is None:
        print "c is none"
    elif d is None:
        print "d is none"
    else:
        print "c is %s,d is %s"% (c,d)
def test1(m ,cmd):
    if cmd not in['start', 'stop']:
        print "the  parameter of cmd: %s is error, the parameter should be 'start' or 'stop' " % cmd
    print "hah"

if __name__ == "__main__":
    test(2, 1, 1, 6)
    test(2, 1)
    test(2, 1, d=7)
    test(1, 3, 4)
    test1(1,'star')