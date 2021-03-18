#!/usr/bin/env python3
import asyncio
from consts import SignalConsts as SIG, Constants as const
from session import Session


# server
clients = {}
sessions = {}

anon = [] # list of connections which have not signed in yet



class ConnectionProtocol(asyncio.Protocol):
    """
    This class is the "user" class. it implements both asyncio callbacks
    (e.g. what to do when a connection is made) and handling of user signals.
    """


    def __init__(self):
        super()
        self.transport = None # the transport object that the server uses to communicate with the client.
        self.current = None # None if not signed in (aka in anon), self if signed in but not in session, Session (object) if in session.




    def connection_made(self, transport):
        """
        This function is the callback called by the server when a new connection is made.
        It recieves the transport object from the server (socket-like)
        """
        self.transport = transport
        anon.append(self)

        self.current = None

    def data_received(self, data):
        """
        The callback called when data is recieved.
        calls the appropriate signal handler.
        """
        data = data.decode()
        signal = int(data[:3])
        msg = data[3:]


        handle_signal = { # dictionary matching signals the user can send to functions that handle them.
            SIG.MESSAGE : self.handle_message,
            SIG.LOGIN : self.log_in
        }
        handle_signal[signal](msg)


    def connection_lost(self, exc):
        """
        The callback for when the connection is lost.
        Cleans up the server lists by checking if a user is in a session, signed in or not.
        """
        if isinstance(self.current, Session):
            self.current.removeUser(self)
        elif self.current == self:
            del super.clients[self]
        else:
            anon.remove(self)

    def log_in(self, username):
        """
        Mockup version of log in (pre database).
        makes sure name length is fine and not already connected.
        """
        if len(username) < 3 or len(username) > 9:
            self.send(SIG.BAD_NAME_LENGTH)
        elif username in clients:
            self.send(SIG.USERNAME_TAKEN)
        else:
            clients[username] = self
            print(username, "connected")

    def handle_message(self, msg):
        """
        Checks if user is host of session and sends msg to session.
        """
        pass

    def send(self, signal, msg=""):
        """
        function used to send signals and messages to client.
        """
        self.transport.write(str(str(signal) + msg).encode())


if __name__ == '__main__':
    print("starting up..")

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ConnectionProtocol, port=const.PORT)
    server = loop.run_until_complete(coro)

    for socket in server.sockets:
        print("serving on {}".format(socket.getsockname()))

    loop.run_forever()
