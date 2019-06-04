#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/16
# @Author  : halliewu
# @File    : test1.py

import tornado.ioloop
import tornado.web
#
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         import time
#         time.sleep(10)
#         self.write("Hello, world")
#
#
# class IndexHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Index")
#
#
# application = tornado.web.Application([
#     (r"/main", MainHandler),
#     (r"/modefy", IndexHandler),
# ])

# print "add first and code"
def test(m ,n ,c=None):
    if m>n:
        # print 'ok'
        try:
            print m/n
        except:
            print "diversion error"
        else:
            print "hhah"
        finally:
            print m
    if m>c:
        print 'error111111'
test(2,0,1)


# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()
