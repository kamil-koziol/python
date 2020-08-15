import hashlib
import os
from base64 import b64encode
from typing import Sequence
import random
from typing import Optional

class Hasher:

    hashIterations = 100000
    saltSize = 128
    hashLen = 128

    @staticmethod
    def checkPassword(password: str, pwdhash: str) -> bool:
        salt = pwdhash[Hasher.hashLen:]
        hashedPassword = Hasher.hashPassword(password, salt=salt)
        print(pwdhash, "\n",hashedPassword)
        return hashedPassword == pwdhash

    @staticmethod
    def hashPassword(password: str, salt: str = None) -> str:
        if not salt:
            salt = os.urandom(Hasher.saltSize).hex()
        myHash = hashlib.pbkdf2_hmac("sha512", bytes(password, "utf-8"), bytes(salt, "utf-8"), Hasher.hashIterations).hex()
        return myHash+salt

    @staticmethod
    def randomSecretKey(length: int = 16) -> str:
        chars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')

        if length < 16:
            raise Exception("Secrets should be at least 128 bits")
        

        return ''.join(random.choice(chars) for _ in range(length))