import socket
from pickle import loads, dumps
from SignalConsts import SignalCosnts as SIG



"""
describes the user class
"""
class User():
    def __init__(self, name, socket):
        self.name = name
        self.socket = socket
        self.session = None

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

    def __eq__(self, value):
        return self.name == value

    def getSignal(self):
        try:
            return loads(self.socket.recv(1024))
        except: # ignore if no signal to get
            pass

    def sendSignal(self, signal): 
        try:
            self.socket.send(dumps(signal))
        except IOError:
            self.disconnect(self, SIG.CONNECTION_BROKE)
            return SIG.CONNECTION_BROKE

    def disconnect(self, reason):
        """
        attempt to inform user of disconnect.
        remove from session if exists, close if host.
        """
        try:
            if self.session == self.name:
                self.session.close() # close the sessions
            
            elif self.session: # if the user is in a session
                self.session.removeUser(self) #disconnect him
            try:
                self.sendSignal(reason)    
                self.socket.close() # and close the connection
            except:
                pass
            del self # delete the user object
        except:
            pass
