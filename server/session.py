import socket

'''
Basic Algorithm:
1) gets host user obj (inits session)
2) opens audio (for now text) stream to host socket and loops over it
3) send the data to each socket in socket list
4) at the beginning of each loop, check for server instructions (e.g. add socket to socket list, remove it or close the session)
'''

class Session():
    def __init__(self, host):
        self.host = host # holds the host (User obj) of the session
        self.users = [] # holds the users in the session
        # maybe add a thread as property


    # adds user to session
    def addUser(self, user):
       self.users.append(user)
       user.session = self

    # disconnect user
    def removeUser(self, user):
        self.users.remove(user)
    
    def run(self):
        pass

    def close(self): # send apropriate disconnect messages to users
        pass

    



