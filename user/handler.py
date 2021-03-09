from SignalConsts import SignalConsts as SIG
from user import login


class Handler:
    # informs user that username is taken and prompts him to try again
    def usernameTaken(*ignore): # does not accept arguments, but doesn't crash if given any.
        print("That username is already taken. please enter a new one.")
        login()












    signals = {
        SIG.USERNAME_TAKEN : usernameTaken
    }