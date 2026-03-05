from . import hashGenerator
from databaseManager import databaseManager 
from . import masterPassword

class AppDriver:

    _hashGen = None
    _databaseManager = None
    _masterPassword= None

    def __init__(self):
        self.__hashGen = hashGenerator.hashGeneratorInstance
        self._databaseManager  = databaseManager.databaseManagerInstance
        self._masterPassword = masterPassword.masterPasswordInstance

    def retrievePassword(self):
        print("Called retrieve password")

    def addPassword(self):
        print("Called add password")

    def changePassword(self):
        pass

    def removePassword(self):
        pass

    def changeMasterPassword(self):

        key , salt = self.__hashGen.generateKey(input("Choose a new master password: "))
        self._databaseManager.setMasterPassword(salt, key)
        self._masterPassword.setMasterPassHash(key)
        self._masterPassword.setSalt(salt)



        
    def showServiceList(self):
        pass

    def exitApp(self):
        pass

appDriverInnstance = AppDriver()