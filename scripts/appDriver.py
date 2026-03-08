from . import hashGenerator
from databaseManager import databaseManager 
from . import masterPassword
import pyperclip

class AppDriver:

    _hashGen = None
    _databaseManager = None
    _masterPassword= None

    def __init__(self):
        self._hashGen = hashGenerator.hashGeneratorInstance
        self._databaseManager  = databaseManager.databaseManagerInstance
        self._masterPassword = masterPassword.masterPasswordInstance

    def retrievePassword(self):
        serviceName = input("Enter the name of the service: ")
        hashedPassword = self._databaseManager.retrievePasswoordHashFromDB(serviceName)
        decryptedPassword = self._hashGen.decryptHash(hashedPassword , self._masterPassword.getMasterPassHash())

        pyperclip.copy(decryptedPassword)

    def addPassword(self):
        serviceName = input('Enter the name of the service (Ex:Gmail): ')
        username = input('Enter the username for the service: ')
        rawPassword = input('Enter the password of the service: ')

        encrypedPassword = self._hashGen.generateHash(rawPassword, self._masterPassword.getMasterPassHash())
        # decryptedPassword = self._hashGen.decryptHash(encrypedPassword , self._masterPassword.getMasterPassHash())

        self._databaseManager.addPasswordToDatabase(serviceName, username, encrypedPassword)

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