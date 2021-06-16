import sys
import os
import platform
from time import sleep

gitrepo = 'https://github.com/le3ch-tech/Simplified-RAT.git'

def pyfi_install_():
    if os.name == 'nt':
        pyfi_install_ = 'pip install pyfiglet'
        return pyfi_install_
    else:
        pyfi_install_ = 'python3 -m pip install pyfiglet'
        return pyfi_install_

try:
    import pyfiglet
    from gui.front import *
    from server.access_point import *
except ModuleNotFoundError:
    print('Modules not installed!')
    sleep(1)
    if ModuleNotFoundError() == gui.front | ModuleNotFoundError() == server.access_point:
        print('GUI or SERVER isnt installed. Please reinstall')
        print('git clone: {}'.format(gitrepo))
        print('Closing in 3 seconds')
        sleep(3)
        exit()
    else:
        print('Module: Pyfiglet not installed.')
        print('Would you like to install it?')
        pyfi_ = input('Y / N')
        if pyfi_ == 'y' | pyfi_ == 'Y':
            print('Installing...')
            sleep(1)
            system.os(pyfi_install_())
        else:
            print('Closing in 3 seconds')
            sleep(3)
            exit()
            
            