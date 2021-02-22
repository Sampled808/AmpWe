#!/usr/bin/env python3

import socket
from session import Session
from user import User
from pickle import loads, dumps

from SignalConsts import SignalCosnts as SIG
#import threading

"""
Sessions manager algorytm:
store sessions in a dict of "host":"thread"
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
        try:
            name = loads(conn.recv(1024))
        except Exception as e:
            print(e)
        print(name + " tries to connect from" + str(addr)) # only for debugging
        

        if name not in users: # make sure there is no other user with that name
            return User(name, conn)
        else:
            conn.send(dumps(SIG.USERNAME_TAKEN))
            conn.close()
            print("name", name, "already taken") # Debug


    
    except IOError as e:
        return None


"""
handles signals from users.
signal numbers are in SignalConsts.py
"""
def handleSignal(user, signal, users, sessions):
    
    if signal == SIG.DISCONNECT:
        n = user # Debug
        try:
            users.remove(user) # remove from users list. can raise ValuError if not in list (shouldn't happen)

            if user.session == user.name: # if the user is a host of a session
                sessions.remove(user) # remove it from sessions
            
            user.disconnect(SIG.OK)
        
        except Exception as e: # make less general
            print(e, user)
            try:
                del user
                print("user deleted")
            except:
                print("error")
            
        print(n, "disconnected") # Debug
        return




        

def main():
    # main server socket
    IP = '127.0.0.1'
    PORT = 8888


    # init main socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setblocking(0)
    serverSocket.bind((IP, PORT))

    # loop over main socket to manage sessions and users
    sessions = [] 
    users = [] 

    serverSocket.listen(5)
    while True:
        # accept new connections
        new = newConnection(serverSocket, users)
        if new:
            users.append(new)
            print(users) # Debug



        for user in users:
            signal = user.getSignal()
            if signal:
                handleSignal(user, signal, users, sessions)


if __name__ == "__main__":
    main()