#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019/5/29
# @Author  : halliewu
# @File    : tornado.py

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")
def make_app():
    return tornado.web.Application([(r"/",MainHandler),])
def main():
    app=make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

