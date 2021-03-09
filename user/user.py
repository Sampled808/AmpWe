#!/usr/bin/env python3

import socket
from SignalConsts import SignalConsts as SIG
from handler import Handler

IP = '127.0.0.1'
PORT = 8888

class 


def handleSignal(signal, *args):
    Handler.signals[signal](args)


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stop sending socket in connect if global, or make socket not global

def send(msg):
    # add checks to see that message is legal (min/max length of name etc)
    # 
    soc.send(str(len(msg)).encode('UTF-8'))
    soc.send(msg.encode('UTF-8'))

def recieve(length):
    sig = soc.recv(length).decode('UTF-8')
    print("recieved", sig)
    if sig.isdigit(): 
        return sig # maybe call handleSignal() from here?
    else:
        return -1 # handle odd messages in the future


def connect(name):
    try:
        soc.connect((IP, PORT))
        print("messaging server")
        send(name)
        print("sent", name)
        return recieve(3)
    except ConnectionRefusedError:
        print("The server is not up right now, please try again later.")
        exit()
    except Exception as e:
        print("connect", e)
        exit()

def login():
    try:
        name = input("Username: ")
        rec = connect(name)
        while rec != SIG.OK:
            print(rec)
            handleSignal(rec)
    except Exception as e:
        print("login", e)

    print("connected to server")
    return 
        

def main():
    login()
    
    


if __name__ == "__main__":
    main()