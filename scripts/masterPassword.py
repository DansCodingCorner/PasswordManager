class MasterPassword:

    masterPasswordHash = "Apple"

    def __init__(self):
        #Will set the password hash later retrieving it from the database
        pass
    
    def checkMatch(self, enteredPassword):
        if enteredPassword == self.masterPasswordHash:
            return True
        else:
            return False
        
    def getMasterPassHash(self):
        return self.masterPasswordHash
    
    def setMasterPassHash(self, masterPasswordHash):
        self.masterPasswordHash = masterPasswordHash

