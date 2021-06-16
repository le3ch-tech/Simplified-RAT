import sys
import os
import platform
from time import sleep

gitrepo = 'https://github.com/le3ch-tech/Simplified-RAT.git'

try:
    import pyfiglet
    from gui.front import *
    from server.access_point import *
except ModuleNotFoundError:
    print('Modules not installed!')
    sleep(1)
    if ModuleNotFoundError() == gui.front:
        print('GUI isnt installed. Please reinstall')
        print('git clone: {}'.format(gitrepo))
        print('closing in 3 seconds')
        sleep(3)
        exit()
    