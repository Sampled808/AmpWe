"""
Signal Constants
"""
class SignalConsts:
    # user requests start from 100
    LOGIN = 100
    SESSION_JOIN = 101
    SESSION_LEAVE = 102
    SESSION_START = 103
    SESSION_CLOSE = 104

    MESSAGE = 120

    # server responses start at 200
    OK = 200


    # client errors start at 400
    USERNAME_TAKEN = 400
    NOT_A_HOST = 401
    MSGLEN_EXPECTED = 403
    BAD_NAME_LENGTH = 404


    # server/connection errors start at 500
    CONNECTION_BROKE = 500
    MESSAGE_NOT_RECIEVED = 501

class Constants:
    # Server's Constants

    IP = '127.0.0.1'
    PORT = 8888
