#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/8
# @Author  : halliewu
# @File    : cluster_config.py
def test(m, n, c=None, d=None):
    # if m>n:
    #     print 'ok'
    # if m>c:
    #     print 'error'
    if c is None and d is None:
        if m == 1:
            print "m=1"
            print "all none"
    elif c is None:
        print "c is none"
    elif d is None:
        cmdline = "%s %s %s %s" % (m, n, c, d)
        print "d is none"
        print cmdline

    else:
        print "c is %s,d is %s" % (c, d)
def test1(m, n, c=None):
    # if m>n:
    #     print 'ok'
    # if m>c:
    #     print 'error'
    print c
    if c is None :

         print "all none"
    else:
        print c
        print m
        print n


# def test_so(file):
#     so_list = []
#     with open(file, 'r') as sofile:
#         for line in sofile.readlines():
#             soline = line.strip()
#             so_list.append(soline)
#     return so_list
# def set_so(is_online,file,str):
#     if is_online:
#         print 1
#     else:
#         print 0
#     start = str.find("Online So")
#     end = str.find("Offline So")
#     # print str[start:end].strip()
#     so_list=test_so(file)
#     server_ips = ["10.208.133.14"]
#     check_result = False
#     for so in so_list:
#         print so
#         for server_ip in server_ips:
#             check_str = "[%s] in [%s" % (so, server_ip)
#             # print check_str
#             if check_str in str:
#                 check_result = True
#     # print check_result
#     # print not check_result
#     print is_online and not check_result
#     if is_online and not check_result:
#         err_msg = "set so online failed."
#         print err_msg
#
#
#     print not is_online
#     print check_result
#
#     if not is_online and not check_result:
#         err_msg = "set so offline failed."
#         print err_msg
#


if __name__ == "__main__":
    c=1
    test1(3,4,c)
    TRCS_IP_PORT_STEST="10.198.143.99:10001"
    master_port = TRCS_IP_PORT_STEST.split(":")
    print type(master_port)
    print master_port
    # test(2,1,1,6)
    # test(2, 1)
    # test(2,1,d=7)
    # m=1
    # test(m,3)
    # TRCS_IP_PORT_STEST = "10.198.143.99:10001"
    # print TRCS_IP_PORT_STEST.split(":")[0]
    # test1=(0, ' \r\n')
    # print test1[0]
    # file="/Users/hallie/project/test/test_file"
    #
    # ONLINE = 1
    # OFFLINE = 0
    #
    # str = "Online So:[603.1.0] in [10.208.133.14-60336]   [609.1.0] in [10.208.133.14-60336] [501.0.0] in [10.208.133.14-60336]Offline So:"
    #
    # set_so(OFFLINE, file, str)

