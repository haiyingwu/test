#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/18
# @Author  : halliewu
# @File    : decorate.py
import time

#
# def timeit(func):
#     def wrapper():
#         start = time.clock()
#         func()
#         end = time.clock()
#         print 'used:', end - start
#
#     return wrapper
#
# @timeit
# def foo():
#     print 'in foo()'
#
# foo()
from xml.dom import minidom
print 'hehe'
print "hh"
def test(i):
    if i==2:
        print 'ok'
    print 'error'
test(2)

import commands
so_list = {}
machine_ip={}
so_xml="/Users/hallie/project/test/test.xml"
ret, out = commands.getstatusoutput('cat /Users/hallie/project/test/test.xml')
# # print out
# print so_xml
so_doc = minidom.parse(so_xml)

online_so_nodes = so_doc.documentElement.getElementsByTagName('Set')
print "online_so_nodes"
print online_so_nodes

for online_so_node in online_so_nodes:
    module_nodes = online_so_node.getAttribute('module_name')

    so_list[module_nodes]=[]
    machine_ip[module_nodes]=[]
    print "module_nodes:%s" % module_nodes
    so_nodes=online_so_node.getElementsByTagName('so')
    machine_nodes = online_so_node.getElementsByTagName('machine')

    for so_node in so_nodes:
        so_list[module_nodes].append(so_node.getAttribute('algid'))
    for machine_node in machine_nodes:
        machine_ip[module_nodes].append(machine_node.getAttribute('ip'))

print so_list
print machine_ip
