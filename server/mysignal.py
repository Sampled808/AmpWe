from user import User
from session import Session
from SignalConsts import SignalConsts as SIG

"""
consts
"""
class Handler:
    def __init__(self):
        pass
    
    LEN_BUFFER = 4 # gets the message length

    def disconnect(self, user, users, sessions):
                n = user # Debug
                try:
                    users.pop(user.name) # remove from users list. can raise ValuError if not in list (shouldn't happen)

                    if user.session == user.name: # if the user is a host of a session
                        sessions.pop(user.name) # remove it from sessions
                    
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


    def sessionStart(self, user, users, sessions):
        # maybe add checks to see if session already exists for some reason
        sessions[user.name] = Session(user.name)
        user.joinSession(sessions[user.name])


    def message(self, user, users, sessions):
        if user.session.host == user.name:
            try:
                mlen = user.socket.recv(LEN_BUFFER)
                msg = (user.socket.recv(mlen))
                user.session.message(mlen, msg)
                user.sendSignal(SIG.OK)
                return
            except:
                user.sendSignal(SIG.MESSAGE_NOT_RECIEVED)
                return
            
        try:
            user.sendSignal(SIG.NOT_A_HOST)
        except:
            pass
            # add test to check if connection still alive?

    def sessionJoin(self, user, users, sessions):
        if not user.session:
            try:
                name = user.socket.recv(9) # 9 is max name length
                session = sessions.get(name)
                if session:
                    user.sendSignal(session.addUser(user))
                return
            except:
                user.sendSignal(SIG.MESSAGE_NOT_RECIEVED)
                return
            
        try:
            user.sendSignal(SIG.NOT_A_HOST)
        except:
            pass
            # add test to check if connection still alive?