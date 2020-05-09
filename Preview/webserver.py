#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    webserver.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.05.08   9:04
-------------------------------------------------------------------------------
   @Change:   2020.05.08
-------------------------------------------------------------------------------
"""


import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()

