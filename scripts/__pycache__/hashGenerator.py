class HashGenerator:

    def __init__(self):
        pass

    def encrypt():
        pass

    def decrypt():
        pass


import os
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
salt = os.urandom(16)
# derive
kdf = Argon2id(
    salt=salt,
    length=32,
    iterations=1,
    lanes=4,
    memory_cost=64 * 1024,
    ad=None,
    secret=None,
)

#This function generates a ket using KDF based on the input password

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b"password"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=1_200_000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
print(key)

f = Fernet(key)
print(f)

token = f.encrypt(b"Secret message!")
print(token)

b'...'
print(f.decrypt(token))
