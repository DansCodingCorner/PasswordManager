from scripts import appDriver
import sys

class UIManager:

    _appDriver = None

    def __init__(self):
        self._appDriver = appDriver.appDriverInnstance

    def printMenu(self):
        '''
        Prints the main menu options.
        '''
        
        selection  = ""
        while selection != "7":
            input("Press Enter to continue...")
            print(f'''Select an option:
                1: Retrieve a password
                2: Add a password
                3: Chage a Password
                4: Remove a password
                5: Change Master Password
                6: Show Service List
                7: Exit
                8: Reset the system
                ''')

            selection  = input(">>>")

            match selection:
                case "1":
                    self._appDriver.retrievePassword()
                case"2":
                    self._appDriver.addPassword()
                case"3":
                    self._appDriver.changePassword()

                case "4":
                    self._appDriver.removePassword()

                case "5":
                    self._appDriver.changeMasterPassword()

                case "6":
                    self._appDriver.showServiceList()
                case "7":
                    print("Exiting system")
                    sys.exit()
                case "8":
                    self._appDriver.resetApp()
                case _:
                    print("Invalid option, please enter a vliad selection.")

uiInstance = UIManager()
