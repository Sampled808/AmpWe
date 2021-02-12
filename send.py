#!/usr/bin/env python3

"""
simple script to use as clients socket.
"""

# socket constants. will be replaced by arguments later
IP = '127.0.0.1'
PORT = 6789


# do on import
import socket

def getsoc():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((IP, PORT))
    return soc


def sendbytes(sock, data):
    sock.send(data)
