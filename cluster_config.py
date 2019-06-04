#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/1/8
# @Author  : halliewu
# @File    : cluster_config.py
import const
import commands
import logging


def choose_config_server(idc):
    if idc == const.IDC_NAME_ATSP:
        cs_addr = const.CONFIG_SERVER_IP_PORT_ASTP
    elif idc == const.IDC_NAME_DT:
        cs_addr = const.CONFIG_SERVER_IP_PORT_DT
    elif idc == const.ENV_STEST_IDC_NAME:
        cs_addr = const.CONFIG_SERVER_IP_PORT_STEST
    else:
        cs_addr = ''
    return cs_addr

def choose_zk_server(idc):
    if idc == const.IDC_NAME_ATSP:
        zk_addr = const.ZK_SERVER_IP_PORT_ASTP
    elif idc == const.IDC_NAME_DT:
        zk_addr = const.ZK_SERVER_IP_PORT_DT
    elif idc == const.ENV_STEST_IDC_NAME:
        zk_addr = const.ZK_SERVER_IP_PORT_STEST
    else:
        zk_addr = ''
    return zk_addr


def check_clusterconfig_result(ret, out_err):
    if "already existed" in out_err:
        logging.warning("clusterconfig warning, the so already exists in set")
        return 0
    if "not existed" in out_err:
        logging.warning("clusterconfig warning, the so to be offlined does not exist in set")
        return 0

    if "error" in out_err or "failed" in out_err or ret != 0:
        logging.error("clusterconfig failed , errcode [%s], msg [%s]" % (ret, out_err))
        return -2
    return 0


def operate_so_file(idc, cluster, set1, so, cmd):
    '''
    so_cmd: /data/home/rtrs/astpserver/client/bin/client/soOper.sh  -cs ip:port -idc xxx -set xxx -on_f/-off_f file
    so 是文件，一行一个so
    '''
    idc_para = "-idc %s" % cluster
    set_para = "-set %s" % set1
    if cmd == "on":
        so_para = "-on_f %s" % so
    elif cmd == "off":
        so_para = "-off_f %s" % so
    else:
        return -2
    cs_para = "-cs %s" % choose_config_server(idc)

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "soOper.sh" + " " + cs_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix, \
                               idc_para, \
                               set_para, \
                               so_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret


def operate_so(idc, cluster, set1, so, cmd):
    '''
    so_cmd: /data/home/rtrs/astpserver/client/bin/client/soOper.sh  -cs ip:port -idc xxx -set xxx -on/-off xxx,xxx
    -on/off 后面是具体的so,多个so以逗号隔开
    '''
    idc_para = "-idc %s" % cluster
    set_para = "-set %s" % set1
    if cmd == "on":
        so_para = "-on %s" % so
    elif cmd == "off":
        so_para = "-off %s" % so
    else:
        return -2
    cs_para = "-cs %s" % choose_config_server(idc)

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "soOper.sh" + " " + cs_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix, \
                               idc_para, \
                               set_para, \
                               so_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret


def update_conf_cmd(idc, cluster, set1, conf_str):
    '''
    conf_str: "-sys /data/home/rtrs/clusterconfig_astp/xxx -route /data/home/rtrs/clusterconfig_astp/yyy"
    update_conf_cmd: /data/home/rtrs/astpserver/client/bin/client/updateConfig.sh -cs ip:port -idc xxx -set xxx -sys xxx
    -cache xxx -route xxx
    '''
    idc_para = "-idc %s" % cluster
    set_para = "-set %s" % set1
    cs_para = "-cs %s" % choose_config_server(idc)

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "updateConfig.sh" " " + cs_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix, \
                               idc_para, \
                               set_para, \
                               conf_str)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret


def get_set_info(idc, cluster, set1, alternate=None):
    """
    query set: ./query.sh -cs ip：port -idc xxx -set xxx
    query cluster:./query.sh -cs ip：port -idc xxx
    """
    if alternate is None:
        cs_para = "-cs %s" % choose_config_server(idc)
    else:
        cs_para = "-cs %s" % const.CONFIG_SERVER_IP_PORT_STEST_Alternate
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "query.sh" + " " + cs_para
    if set1 is None:
        cmdline = "%s -idc %s" % (clusterconfig_cmd_prefix, \
                                  cluster)
    else:
        cmdline = "%s -idc %s -set %s" % (clusterconfig_cmd_prefix, \
                                          cluster, \
                                          set1)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    if retcode != 0:
        logging.error("run cmdline [%s] failed, errmsg [%s]" % (cmdline, out.strip()))
        return ""
    return out


def shrink_machine(idc,cluster, set1, iplist, alternate=None):
    """
    appoint shrink:  ./shrinkScale.sh -cs ip:port -idc xxx -set xxx -ipf iplist
    complete shrink: ./shrinkScale.sh -cs ip:prot -idc xxx -set xxx
    """
    idc_para = "-idc %s" % cluster
    set_para = "-set %s" % set1
    if alternate is None:
        cs_para = "-cs %s" % choose_config_server(idc)
    else:
        cs_para = "-cs %s" % const.CONFIG_SERVER_IP_PORT_STEST_Alternate
    if iplist is None:
        ip_para = None
    else:
        ip_para = "-ipf %s" % iplist

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "shrinkScale.sh" + " " + cs_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix,
                                  idc_para,
                                  set_para,
                                  ip_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret


def expand_machine(idc,cluster, set1, iplist, alternate=None):
    """./assignScale.sh -cs ip:port -idc xxx -set xxx -ipf iplist"""
    idc_para = "-idc %s" % cluster
    set_para = "-set %s" % set1
    ip_para = "-ipf %s" % iplist
    if alternate is None:
        cs_para = "-cs %s" % choose_config_server(idc)
    else:
        cs_para =  "-cs %s" % const.CONFIG_SERVER_IP_PORT_STEST_Alternate

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH +"/"+"assignScale.sh"+ " " + cs_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix,
                                  idc_para,
                                  set_para,
                                  ip_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret


def auto_expand_machine(idc, des, iplist, sys, cache, report, route):
    """./autoScale.sh -cs ip:port -des xxx -ipf xxx -sys xxx -cache xxx -report xxx -route xxx """
    cs_para = "-cs %s" %  choose_config_server(idc)
    des_para = "-des %s" % des
    ip_para = "-ipf %s" % iplist
    sys_para = "-sys %s" % sys
    cache_para = "-cache %s" % cache
    report_para = "-report %s" % report
    route_para = "-route %s" % route

    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/"+"autoScale.sh"+" " + cs_para
    cmdline = "%s %s %s %s %s %s %s" % (clusterconfig_cmd_prefix,
                                           des_para,
                                           ip_para,
                                           sys_para,
                                           cache_para,
                                           report_para,
                                           route_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def compare_snapshot(idc,cluster,type,dynamic):
    """
    ./compareSnapshot.sh -cs ip:port -idc xxx -type
    type: pctr/rerank/scoring/mixer
    dynamic: "-d"
    """
    idc_para = "-idc %s" % cluster
    cs_para = "-cs %s" % choose_config_server(idc)
    type_pare="-type %s" % type
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "compareSnapshot.sh" + " " + cs_para
    if dynamic is None:
        is_dynamic=None
    else:
        is_dynamic=dynamic
    cmdline="%s %s %s %s" % (clusterconfig_cmd_prefix,idc_para,type_pare,is_dynamic)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def rebulid_snapshot(idc,cluster,type,dynamic):
    """
    ./rebuildSnapshot.sh -cs ip:port -idc xxx -type
    type: pctr/rerank/scoring/mixer
    dynamic: "-d"
    """
    idc_para = "-idc %s" % cluster
    cs_para = "-cs %s" % choose_config_server(idc)
    type_pare="-type %s" % type
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "rebuildSnapshot.sh" + " " + cs_para
    if dynamic is None:
        is_dynamic=None
    else:
        is_dynamic=dynamic
    cmdline="%s %s %s %s" % (clusterconfig_cmd_prefix,idc_para,type_pare,is_dynamic)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def get_master_node(idc,id):
    """./master.sh -zk ip:port -ns xxx -id xxx"""
    zk_para="-zk %s" % choose_zk_server(idc)
    ns_para="-ns %s" % idc
    id_para="-id &s" % id
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "master.sh" + " " + zk_para
    cmdline="%s %s %s" % (clusterconfig_cmd_prefix,ns_para,id_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def backup_zk(idc,backup_path):
    """./backup.sh -zk ip:port -ns xxx -d path"""
    zk_para = "-zk %s" % choose_zk_server(idc)
    ns_para = "-ns %s" % idc
    dir_para="-d %s" % backup_path
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "backup.sh" + " " + zk_para
    cmdline = "%s %s %s" % (clusterconfig_cmd_prefix, ns_para, dir_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def recover_zk(idc,node_path,data_path):
    """./recover.sh -zk ip:port -ns xxx -node xxx -data xxx """
    zk_para = "-zk %s" % choose_zk_server(idc)
    ns_para = "-ns %s" % idc
    node_para = "-node %s" % node_path
    data_para="-data %s" % data_path
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "recover.sh" + " " + zk_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix, ns_para, node_para, data_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret

def compare_zk_backup(idc,node_path,data_path):
    """./compare.sh -zk ip:port -ns xxx -node xxx -data xxx """
    zk_para = "-zk %s" % choose_zk_server(idc)
    ns_para = "-ns %s" % idc
    node_para = "-node %s" % node_path
    data_para="-data %s" % data_path
    clusterconfig_cmd_prefix = const.CLUSTERCONFIG_BIN_PATH + "/" + "compare.sh" + " " + zk_para
    cmdline = "%s %s %s %s" % (clusterconfig_cmd_prefix, ns_para, node_para, data_para)
    logging.debug("the clusterconfig cmdline is %s" % cmdline)
    retcode, out = commands.getstatusoutput(cmdline)
    ret = check_clusterconfig_result(retcode, out)
    return ret
