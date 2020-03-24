from .. import *

class PasswordHashSettings(object):
    salt_length = 16    # The length of the salt in bytes.              Default:   16
    key_length  = 32    # The length of the derived key in bytes.       Default:   32
    cost_factor = 1024  # The CPU/Memory cost factor (2 ^ x = cost).    Default: 1024
    block_size  = 8     # The block size in bytes.                      Default:    8
    par_factor  = 1     # The parallelization factor based on the CPU.  Default:    1
    
    def setSaltLength(self, length):
        self.salt_length = length       \
            if getType(length) == 'int' \
            else 16
            
    def setKeyLength(self, length):
        self.key_length = length        \
            if getType(length) == 'int' \
            else 32
            
    def setCostFactor(self, cost):
        self.cost_factor = 2 ** cost    \
            if getType(length) == 'int' \
            else 1024
            
    def setBlockSize(self, value):
        self.block_size = value         \
            if getType(value) == 'int'  \
            else 8
            
    def setParallelFactor(self, value):
        self.par_factor = value         \
            if getType(value) == 'int'  \
            else 1

class PasswordHashClass(PasswordHashSettings):
    __author__      = "Dracovian"
    __prettyname__  = "Security - Password Hash"
    
    def newHash(self, password):
        self.salt  = os.urandom(self.salt_length)
        self.cost  = self.cost_factor
        self.block = self.block_size
        self.par   = self.par_factor
        
        self.hash = scrypt(
            password,
            salt=self.salt,
            n=self.cost,
            r=self.block,
            p=self.par,
            dklen=self.key_length
        )
        
    def getHash(self):
        safe_salt = safeEncode(self.salt)
        safe_hash = safeEncode(self.hash)
        
        return f'S:{self.cost}:{self.block}:{self.par}:{safe_salt}:{safe_hash}'
        
    def verifyHash(self, passhash, password):
        id, cost, block, par, safe_salt, safe_hash = passhash.split(':')
        
        salt = safeDecode(safe_salt)
        hash = safeDecode(safe_hash)
        
        test = scrypt(password, salt=salt, n=int(cost), r=int(block), p=int(par), dklen=self.key_length)
        return hash == test