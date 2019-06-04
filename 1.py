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
# print "hhaaaa"
# def test(i):
#     if i==2:
#         m=3
#         n=5
#         print 'ok'
#     print 'error'
# test(2)

import commands
so_list = {}
set_value={}
so_xml="/Users/hallie/project/test/test1.xml"
ret, out = commands.getstatusoutput('cat /Users/hallie/project/test/test1.xml')
# # print out
# print so_xml
so_doc = minidom.parse(so_xml)

online_so_nodes = so_doc.documentElement.getElementsByTagName('Set')
# print "online_so_nodes"
# print online_so_nodes

for online_so_node in online_so_nodes:
    module_nodes = online_so_node.getAttribute('module_name')

    so_list[module_nodes]=[]
    set_value[module_nodes]=[]
    print "module_nodes:%s" % module_nodes
    so_nodes=online_so_node.getElementsByTagName('so')
    machine_nodes = online_so_node.getElementsByTagName('machine')

    for so_node in so_nodes:
        so_list[module_nodes].append(so_node.getAttribute('algid'))
    for machine_node in machine_nodes:
        print machine_node.getAttribute('ip')
        set_value[module_nodes].append(machine_node.getAttribute('ip'))

    # for i in xrange(len(machine_nodes)):
    #     set_value[module_nodes].append("%s" % machine_nodes[i].getAttribute("ip"))

print so_list
print set_value

# print set_value["set-trcs_pctr1"][0]

# server_ip=['10.208.133.14', '10.208.144.84']
# for ip in server_ip:
#     if ip in set_value['set-trcs_pctr']:
#         print "yes"
#     else:
#         print ip
set_name='set-trcs_pctr'
print set_value.has_key(set_name)
if set_name in set_value.keys():
    print "in"
ip_list=['5','6']
ip0_list=[]
ip0_list.extend(ip_list[0])
print ip0_list

