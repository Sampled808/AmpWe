#!/usr/bin/env python3

import socket
from session import Session
from user import User

from SignalConsts import SignalConsts as SIG
from mysignal import Handler
#import threading

"""
Sessions manager algorytm:
store sessions in a dict of "host":"thread/host"
"""

"""
server accepts new connection.
if the new connection is creating a session it will add a session to connected
otherwise it will link it to existing session.
"""
def newConnection(serverSocket, users):
    try:
        conn, addr = serverSocket.accept()
        conn.setblocking(0)
        return conn

    except IOError as e:
        return None
    
    print(addr)

def recieve(conn, length): # add try except?, make it handle headers/signals?
    p = length if length != 1 else ""
    print(p, end="")
    sig = conn.recv(length).decode('UTF-8')
    if sig.isdigit(): 
    
        print("recieved num", sig)
        return int(sig) # maybe call handleSignal() from here?

    elif not sig:
        return
    else:

        print("recieved str", sig)
        return sig

def tryLogin(conn, users):
    name = ""
    mlen = None
    try:
        try:
            mlen = recieve(conn, 1)
        except:
            return
        if not mlen:
            return
        elif type(mlen) is not int:
            conn.send(str(SIG.MSGLEN_EXPECTED).encode()) # add handler on user end
            conn.close()
        
        elif int(mlen) < 3: # name length between 3 and 9
            print("bad length") # debug
            conn.send(str(SIG.BAD_NAME_LENGTH).encode())
        
        else: 
            print("listening for name")
            name = recieve(conn, mlen) 

    except Exception as e:
        print("trylogin"e)
    if not name:
        return
    elif name not in users: # make sure there is no other user with that name
        print(name + " connected") # only for debugging
        user = User(name, conn)
        user.sendSignal(SIG.OK)
        return user
    else:
        conn.send(str(SIG.USERNAME_TAKEN).encode())
        print("name", name, "already taken") # Debug
        return

"""
handles signals from users.
signal numbers are in SignalConsts.py
"""

signals = {
        SIG.DISCONNECT : Handler.disconnect,
        SIG.SESSION_START : Handler.sessionStart
}

def handleSignal(user, signal, users, sessions):
    signals[signal](user, users, sessions)



        

def main(serverSocket):
    # main server socket
    IP = '127.0.0.1'
    PORT = 8888


    # init main socket
    serverSocket.setblocking(0)
    serverSocket.bind((IP, PORT))

    # loop over main socket to manage sessions and users
    # maybe should be dicts
    sessions = {}
    users = {}
    anon = [] # new connections not yet signed in

    serverSocket.listen(5)
    while True:
        # accept new connections
        new = newConnection(serverSocket, users)
        if new:
            anon.append(new)



        for name, user in users.items():
            signal = user.getSignal()
            if signal:
                handleSignal(user, signal, users, sessions)

        for u in anon:
            u = tryLogin(u, users)
            if u:
                users[u.name]=u
                anon.remove(u.socket)



if __name__ == "__main__":
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        main(serverSocket)
    except  Exception as e: # KeyboardInterrupt
        
        serverSocket.close()
        raise e

    else:
        serverSocket.close()