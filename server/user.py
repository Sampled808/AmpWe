import socket
from SignalConsts import SignalConsts as SIG



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
            return int(self.socket.recv(3).decode('UTF-8'))
        except IOError: # ignore if no signal to get
            pass
        except ValueError:
            pass # handle case of signal being non-numeral
        except UnicodeDecodeError:
            pass # handle message not being utf-8

    def sendSignal(self, signal): 
        try:
            self.socket.send(str(signal).encode())
        except IOError:
            self.disconnect(self, SIG.CONNECTION_BROKE) # INFINITE LOOP ALERT
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

    def joinSession(self, session):
        # maybe add checks to see if user already in session
        # after adding the database check that the user can join that session (in friends list and session isnt invite only etc)
        self.session = session
        self.sendSignal(SIG.OK)