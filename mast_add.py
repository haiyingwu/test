#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/20
# @Author  : halliewu
# @File    : mast_add.py
# print "master"
# import os
#
# def new_report(test_report):
#     lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
#     print(lists)
#     lists.sort(key=lambda fn:os.path.getmtime(test_report + "/" + fn))#按时间排序
#     file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new
#     print(file_new)
#     return file_new
import logging


def get_list(so_file):
    result_list = []
    with open(so_file, 'r') as do_file:
        for so_line in do_file.readlines():
            so_line = so_line.strip()
            result_list.append(so_line)
    return result_list


if __name__ == "__main__":
    test_report = "/Users/hallie/project"  # 目录地址
    # new_report(test_report)
    # print new_report(test_report)+"/"+"test1"
    import time
    import os

    server_ips = ['10.208.133.14','10.208.144.84']
    # ip_dict={'i':server_ip}
    # timestamp = int(time.time())
    # iplist_file_tmp = "iplist.%s" % timestamp
    # iplist = '/Users/hallie/project/test/' + iplist_file_tmp
    # with open(iplist, 'w') as iplist_file:
    #     iplist_file.write(server_ip[0])
    #     iplist_file.write('\n')
    #
    # print type(iplist)
    # print type(server_ip[0])
    # print str(server_ip)
    # print str(server_ip).replace("'",'').strip('[').strip(']').replace(' ',"")
    # str=''
    # for i in server_ip:
    #    str=str+i+','
    # print str
    # if isinstance(server_ip,list):
    #     print 'hha'
    #     print str(server_ip).replace("'",'').strip('[').strip(']').replace(' ',"")
    # m='10.208.133.14,10.209.34.56,10.209.3.4'
    # print "-on %s" % m
    # so=['10.208.133.14','10.209.34.56','10.209.3.4']

    so_file = '/Users/hallie/project/test/test_file'
    so_list = get_list(so_file)
    if isinstance(so_list, list):
        print 'hah'
        so = str(so_list).replace("'", '').strip('[').strip(']').replace(' ', "")
    so_para = "-%s %s" % ('cmd', so)
    print so_para

    # if server_ip.index(i)==len(server_ip)-1:
    #     print (i)
    # else:
    #     print (i+","),
    # print '-ip %s' % server_ip[0]
    # if os.path.isfile(server_ip) :
    #     print 'true'

# if __name__ == "__main__":
#     test(2, 1, 1, 6)
#     test(2, 1)
#     test(2, 1, d=7)
#     test(1, 3, 4)

# def get_snapshop_value(idc, cluster, snapshot_type, so_machine):
#     # 获取快照中的ip和so
#
#     if so_machine == "so":
#         tag_name = "so"
#         node_value = "algid"
#     elif so_machine == "machine":
#         tag_name = "so"
#         node_value = "algid"
#     else:
#         err_msg = "parameter error,should be so or machine"
#         logging.error(err_msg)
#         return -1, err_msg
#
#     set_value = {}
#     zk_ip = const.ZK_SERVER_IP_PORT_STEST
#     zkhandler = ZkConf(zk_ip)
#     path = "%s/%s/%s/napshot-%s" % (zkhandler.root_path, cluster, idc, snapshot_type)
#     logging.debug("the path in zk to be checked is %s" % path)
#     set_info = zkhandler.get(path)
#     xmlhander = xmlHandler(set_info, const.XML_FORMAT_STRING)
#     if xmlhander.status != const.XML_OBJ_NORMAL:
#         logging.error("failed to get snap_shot")
#         zkhandler.close()
#         return set_value
#     else:
#         set_tags = xmlhander.root.getElementsByTagName("Set")
#         for set_tag in set_tags:
#             module_nodes = set_tag.getAttribute('module_name')
#             set_value[module_nodes] = []
#             machine_tag = xmlhander.root.getElementsByTagName(tag_name)
#             for i in xrange(len(machine_tag)):
#                 set_value[module_nodes].append("%s" % machine_tag[i].getAttribute(node_value))
#         logging.debug("the set_value list is %s" % set_value)
#         zkhandler.close()
#         return set_value
so_output = "[3033.900.0] in [10.208.133.14-60336]" \
            "[602.1.0] in [10.208.133.14-60336]" \
            "[601.1.0] in [10.208.133.14-60336]" \
            "[3033.900.0] in [10.208.144.84 - 60336]" \
            "[602.1.0] in [10.208.144.84 - 60336]" \
            "[601.1.0] in [10.208.144.84 - 60336]"
snapshot_so_static={u'set-trcs_pctr': [u'3033.900.0', u'601.1.0', u'602.1.0'], u'set-trcs_pctr1': [u'3033.900.0', u'601.1.0', u'602.1.0']}
snapshot_so_dynamic={u'set-trcs_pctr': [u'3033.900.0', u'601.1.0', u'602.1.0'], u'set-trcs_pctr1': [u'3033.900.0', u'601.1.0', u'602.1.0']}
so_list=[u'3033.900.0', u'601.1.0', u'602.1.0']
check_result=False
for so in so_list:
    for server_ip in server_ips:
        check_str = "[%s] in [%s" % (so, server_ip)
        # print 'check_str:%s' % check_str
        # print check_str in so_output
        print so in snapshot_so_static['set-trcs_pctr1']
        if check_str in so_output and so in snapshot_so_static['set-trcs_pctr1'] and so in snapshot_so_dynamic[
            'set-trcs_pctr1']:
            check_result = True
print check_result

str = "----cluster snapshot block conf info----cluster:trcs-PCTR-dynamic, active:true, block:false " \
      "block_dir:/data/home/rtrs/trcs-all-1.0.0/server/./block/trcs-PCTR-dynamicQUERY_BLOCK_CONF_MSG deal done'"
check_str="active:true, block:false"
if check_str in str:
    print 'hhah'

# import commands
# # cmd="ls /Users/hallie/Downloads/UFA/img|grep 0|tail -1"
# path="/Users/hallie/project/test"
# cmd1='cd /Users/hallie/Downloads/UFA/img;pwd'
# cmd2="pwd"
# retcode, out1 = commands.getstatusoutput(cmd1)
# retcode, out2 = commands.getstatusoutput(cmd2)
# print out1
# print out2
print os.path.dirname(os.path.abspath(__file__))

