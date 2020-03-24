from modules import *

class MyBooru():
    __author__    = "Dracovian"
    __project__   = "MyBooru"
    __copyright__ = None
    __credits__   = ["Dracovian"]
    __license__   = "BSD"
    __version__   = "0.1"
    __email__     = "25242161+Dracovian@users.noreply.github.com"
            
if __name__ == '__main__':
    passhash = PasswordHash()
    passhash.newHash(b'Onomatopoeia')
    
    hash = passhash.getHash()
    password = input('Enter the password: ')
    
    if passhash.verifyHash(hash, password.encode()):
        print('Password Correct!')
    else:
        print('Password Incorrect!')