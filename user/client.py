#!/usr/bin/env python3

import socket
from consts import SignalConsts as SIG

IP = '127.0.0.1'
PORT = 8888


class Handler:
    # informs user that username is taken and prompts him to try again
    def usernameTaken(self, *ignore): # does not accept arguments, but doesn't crash if given any.
        print("That username is already taken. please enter a new one.")
        login()

    signals = {
        SIG.USERNAME_TAKEN : usernameTaken
    }

def handleSignal(signal, *args):
    Handler.signals[signal](args)


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# stop sending socket in connect if global, or make socket not global

def send(msg):
    # add checks to see that message is legal (min/max length of name etc)
    #
    # soc.send(str(len(msg)).encode())
    soc.send(msg.encode())

def recieve(length):
    sig = soc.recv(length).decode()
    print("recieved", sig)
    if sig.isdigit():
        return int(sig) # maybe call handleSignal() from here?
    else:
        return -1 # handle odd messages in the future


def connect(name):
    try:
        print("messaging server")
        send(str(SIG.LOGIN) + name)
        print("sent", name)
        return recieve(3)
    except ConnectionRefusedError:
        print("The server is not up right now, please try again later.")
        exit()
    except Exception as e:
        raise e
        exit()

def login():
    try:
        name = input("Username: ")
        rec = connect(name)
        print(rec)
        while rec != SIG.OK:
            handleSignal(rec)
    except Exception as e:
        raise e

    print("connected to server")
    return

def main():
    soc.connect((IP, PORT))
    login()



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        soc.close()
        raise e
