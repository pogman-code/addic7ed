from addic7ed.parser import IncompleteError
from termcolor import colored

def friendly_msg(e):

    if e.__class__ == ValueError:
        print(colored('please enter numbers instead of words', 'yellow'))

    elif e.__class__ == IncompleteError:
        print(colored('please select another subtitle', 'yellow'))

    elif e.__class__ == IOError:
        print(colored('error related with file or user input/output', 'yellow'))

    elif e.__class__ == IndexError:
        print(colored('please input a correct number', 'yellow'))

    elif e.__class__ == PermissionError:
        print(colored('check permissions of this directory', 'yellow'))

    else:
        print(colored('look for the error at: https://docs.python.org/2/library/exceptions.html', 'yellow'))
