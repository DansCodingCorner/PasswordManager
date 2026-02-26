class MasterPassword:

    _salt = b""
    _masterPasswordHashh = b""

    def __init__(self, salt, masterPasswordHash):
        self._salt = salt 
        self._masterPasswordHashh = masterPasswordHash
    

    def checkMatch(self, enteredPassword):

        if enteredPassword == self._masterPasswordHashhmasterPasswordHash:
            return True
        else:
            return False
    

    def getMasterPassHash(self):

        return self._masterPasswordHash
    
    def getSalt(self):

        return self._salt
    
    def setMasterPassHash(self, masterPasswordHash):

        self.masterPasswordHash = masterPasswordHash

