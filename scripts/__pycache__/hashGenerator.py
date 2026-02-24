import os
from cryptography.hazmat.primitives.kdf.argon2 import Argon2id
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class HashGenerator:
    '''
    This class provides the neccessary methods to perform various 
    functions for encrypting passwords and generating encryption keys.
    '''


    def generateHash(self, message : str | bytes, key):
        '''
        This method is used for when adding new passwords that 
        need to be encrypted
        '''
        if type(message) == str:
            message = message.encode("UTF-8")

        f = Fernet(key)

        eencryptedMessage = f.encrypt(message)

        return eencryptedMessage


    def decryptHash(self, eencryptedMessage : bytes, key):

        f = Fernet(key)

        decryptedMessage =f.decrypt(eencryptedMessage)
        decryptedMessage = decryptedMessage.decode()

        return decryptedMessage


    def generateKey(self, eneredPassword, salt = 0):
        '''
        This is used to generate the encrryption key
        from the User's master password, the first time it is run,
        The salt will be generated and can be stored later.
        '''

        passwordBytes = eneredPassword.encode("utf-8")

        if salt == 0:
            salt = self.generateSalt()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(passwordBytes))

        return key, salt
    

    def generateSalt(self):

        salt = os.urandom(16)

        return salt



hg = HashGenerator()

Masterpassword = "Apple"

keySalt  = hg.generateKey(Masterpassword)
key = keySalt[0]
salt = keySalt[1]

newPassword = 'Akmeer123@'


encrypedPasswordHash = hg.generateHash(newPassword, key)
print(encrypedPasswordHash)


decryptedPassword = hg.decryptHash(encrypedPasswordHash, key)
print(decryptedPassword)










