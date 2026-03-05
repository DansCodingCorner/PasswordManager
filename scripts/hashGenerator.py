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


    def generateKey(self, enteredPassword, salt=None):

        passwordBytes = enteredPassword.encode("utf-8")

        if salt is None:
            print("No salt provided, generating new salt")
            salt = self.generateSalt()          # returns bytes
            # salt = base64.urlsafe_b64encode(salt).decode('ascii')

        # else:
        #     # salt came from DB → it's already base64 string
        #     print("Salt from DB (base64 string):", salt)
        #     salt = base64.urlsafe_b64decode(salt)   
            
        print("Salt  being used to generate the key in hashgen: ")
        print(salt)

        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,               # must be bytes
            iterations=1_200_000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(passwordBytes))
        
        # If this was first-time generation, you still need to return the new salt (base64 string)
        if salt is None:
            return key, salt_b64
        else:
            return key, salt
    
    

    def generateSalt(self):

        salt = os.urandom(16)

        return salt


hashGeneratorInstance = HashGenerator()








