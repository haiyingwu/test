#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018/10/16
# @Author  : halliewu
# @File    : test1.py

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        import time
        time.sleep(10)
        self.write("Hello, world")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Index")


application = tornado.web.Application([
    (r"/main", MainHandler),
    (r"/modefy", IndexHandler),
])

print "add first and code"


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()