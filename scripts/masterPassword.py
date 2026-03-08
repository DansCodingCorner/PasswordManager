from databaseManager import databaseManager
from scripts import hashGenerator


class MasterPassword:

    _dbManager = None
    _hashGen = None
    _salt = None
    _masterPasswordHashh = None

    def __init__(self):
        self._dbManager = databaseManager.databaseManagerInstance
        self._salt =  self._dbManager.retieveMasterPasswordSalt()
        self._masterPasswordHashh = self._dbManager.retrieveMasterPasswordHash()
        self._hashGen = hashGenerator.hashGeneratorInstance

      

    def checkMatch(self, enterrePassword):
        '''
        Checks if the entered master password is correct by hashing it with the stored salt and comparing it to the stored master password hash.
        '''

        enteredPasswordHash = self._hashGen.generateKey(enterrePassword, self._salt)

        enteredPasswordHash = enteredPasswordHash[0]

        if enteredPasswordHash == self._masterPasswordHashh:
            return True
        
        else:
            return False
    

    def getMasterPassHash(self):
        '''
        Returns the stored master password hash.
        '''

        return self._masterPasswordHashh
    
    def getSalt(self):
        '''
        Returns the stored salt.
        '''

        return self._salt
    
    def setSalt(self, salt):
        '''
        Sets the salt for the master password. This is used when changing the master password.
        '''

        self._salt = salt
    
    def setMasterPassHash(self, masterPasswordHash):
        '''
        Sets the master password hash. This is used when changing the master password.
        '''

        self._masterPasswordHashh = masterPasswordHash

masterPasswordInstance = MasterPassword()