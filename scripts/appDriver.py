from . import hashGenerator
from databaseManager import databaseManager 

class AppDriver:

    _hashGen = None
    _databaseManager = None

    def __init__(self):
        self.__hashGen = hashGenerator.HashGenerator()
        self._databaseManager  = databaseManager.DatabaseManager()

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

        
    def showServiceList(self):
        pass

    def exitApp(self):
        pass

ad = AppDriver()
