from . import hashGenerator
from databaseManager import databaseManager 
from . import masterPassword
import pyperclip
import sys

class AppDriver:

    _hashGen = None
    _databaseManager = None
    _masterPassword= None

    def __init__(self):
        self._hashGen = hashGenerator.hashGeneratorInstance
        self._databaseManager  = databaseManager.databaseManagerInstance
        self._masterPassword = masterPassword.masterPasswordInstance

    def retrievePassword(self):
        '''
        Retrieves the password for a given service, decrypts it and copies it to the clipboard.
        '''
        serviceName = input("Enter the name of the service: ")
        try:
            hashedPassword = self._databaseManager.retrievePasswoordHashFromDB(serviceName)
            decryptedPassword = self._hashGen.decryptHash(hashedPassword , self._masterPassword.getMasterPassHash())

            pyperclip.copy(decryptedPassword)
            print(f"Password for {serviceName} has been copied to clipboard!")

        except ValueError:
            print(f"Service {serviceName} not found.")
            return

    def addPassword(self):
        '''
        Adds a new password to the database. The password is encrypted before being stored.
        '''

        serviceName = input('Enter the name of the service (Ex:Gmail): ')
        username = input('Enter the username for the service: ')
        rawPassword = input('Enter the password of the service: ')

        encrypedPassword = self._hashGen.generateHash(rawPassword, self._masterPassword.getMasterPassHash())

        self._databaseManager.addPasswordToDatabase(serviceName, username, encrypedPassword)

        print(f"Added password for {serviceName} successfully!")

    def changePassword(self):
        '''
        Changes the password for a given service. The new password is encrypted before being stored.
        '''

        print("Services available: ")
        self.showServiceList()

        serviceName = input('Enter the name of the service you want to change the password for: ')
        rawPassword = input('Enter the new password of the service: ')
        encrypedPassword = self._hashGen.generateHash(rawPassword, self._masterPassword.getMasterPassHash())

        try:
            self._databaseManager.changePassword(serviceName, encrypedPassword)
            print(f"Password for {serviceName} has been updated successfully!")

        except ValueError:
            print(f"Service {serviceName} not found.")
            return



    def removePassword(self):
        '''
        Removes the password for a given service from the database.
        '''
        print("Services available: ")
        self.showServiceList()

        serviceName = input('Enter the name of the service you want to remove: ')
        try:
            self._databaseManager.removePasswordFromDatabase(serviceName)
            print(f"Password for {serviceName} has been removed successfully!")

        except ValueError:
            print(f"Service {serviceName} not found.")
            return

    def changeMasterPassword(self):
        '''
        Changes the master password. This will re-encrypt all the stored passwords with the new master password.
        '''

        key , salt = self._hashGen.generateKey(input("Choose a new master password: "))
        self._databaseManager.setMasterPassword(salt, key)
        self._masterPassword.setMasterPassHash(key)
        self._masterPassword.setSalt(salt)

        print("Your master password has been updated. Please restart the application to start using the new master password!")
        sys.exit()

        
    def showServiceList(self):
        '''
        Displays the list of services for which passwords are stored in the database.
        '''
        serviceList = self._databaseManager.getServiceList()

        print(f'''{"Service Name":<20}{"Username":<20}
{"-"*50}''')
        for service in serviceList:
            print(f"{service[0]:<20}{service[1]:<20}")

    def exitApp(self):
        '''
        Exits the application.
        '''

        print("Thank you! Closing app")
        sys.exit()

    def resetApp(self):
        '''Resets the application by clearing all stored passwords and master password from the database.
        '''
        selection = input("Are you sure you want to reset the system? This action cannot be undone! (y/n): ")
        if selection.lower() != "y":
            print("Resetting system, the applicaation will close now.")    
            self._databaseManager.dropTables()

            sys.exit()
        else:
            print("Rest cancelled, returing to the menu.")

appDriverInnstance = AppDriver()