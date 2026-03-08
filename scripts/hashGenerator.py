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
        '''
        This method is used for when retrieving passwords that are stored in the database. It takes the encrypted password and decrypts it using the master password hash as the key.
        '''

        f = Fernet(key)

        decryptedMessage =f.decrypt(eencryptedMessage)
        decryptedMessage = decryptedMessage.decode()

        return decryptedMessage


    def generateKey(self, enteredPassword, salt=None):
        '''
        This method is used to generate the master password hash and salt. If no salt is provided, it generates a new salt. It returns the generated key and salt (if a new one was generated).
        '''
 
        passwordBytes = enteredPassword.encode("utf-8")

        if salt is None:
            print("No salt provided, generating new salt")
            salt = self.generateSalt()          # returns bytes


        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=1_200_000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(passwordBytes))
        
        if salt is None:
            return key, salt
        else:
            return key, salt
    


    def generateSalt(self):
        '''
        This method generates a random salt using os.urandom and returns it.
        '''

        salt = os.urandom(16)

        return salt


hashGeneratorInstance = HashGenerator()








