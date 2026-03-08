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

        enteredPasswordHash = self._hashGen.generateKey(enterrePassword, self._salt)

        enteredPasswordHash = enteredPasswordHash[0]

        if enteredPasswordHash == self._masterPasswordHashh:
            return True
        
        else:
            return False
    

    def getMasterPassHash(self):

        return self._masterPasswordHashh
    
    def getSalt(self):

        return self._salt
    
    def setSalt(self, salt):

        self._salt = salt
    
    def setMasterPassHash(self, masterPasswordHash):

        self._masterPasswordHashh = masterPasswordHash

masterPasswordInstance = MasterPassword()