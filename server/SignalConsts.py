"""
Signal Constants
"""
class SignalCosnts():
    # user requests start from 100
    DISCONNECT = 100
    SESSION_JOIN = 101
    SESSION_LEAVE = 102
    SESSION_START = 103
    SESSION_CLOSE = 104

    # server responses start at 200
    OK = 200
    
    # client errors start at 400
    USERNAME_TAKEN = 400
    
    # server/connection errors start at 500
    CONNECTION_BROKE = 500