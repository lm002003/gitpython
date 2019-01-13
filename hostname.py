#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# Filename : hello.py
# author by :lium

# 该实例输出 Hello World!

import socket
hostname = socket.gethostname()
print(hostname)
ip = socket.gethostbyname(hostname)
ipList = socket.gethostbyname_ex(hostname)
print(ipList)
