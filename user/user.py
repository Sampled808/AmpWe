#!/usr/bin/env python3
import socket
from pickle import dumps as d
import sys
from SignalConsts import SignalCosnts as SIG
from time import sleep

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('127.0.0.1', 8888))
name = sys.argv[1]
soc.send(d(name))

sleep(3)
soc.send(d(SIG.DISCONNECT))

