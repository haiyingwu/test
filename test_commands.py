#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/10
# @Author  : halliewu
# @File    : test_commands.py
import commands

cmdline_block_static = "sh /data/home/rtrs/astpserver_jak/client/bin/script_test/unblock_restart_trcs.sh >/dev/null 2>&1 &"
print "the clusterconfig cmdline is %s" % cmdline_block_static
retcode, out = commands.getstatusoutput(cmdline_block_static)
print "recode is %s"% retcode
print "out is %s" % out