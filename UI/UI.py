from scripts import masterPassword

class UIManager:

    masterPasswordObject = None

    def __init__(self):
        self.masterPasswordObject = masterPassword.MasterPassword()

    def printMenu(self):
        print(f'''Select an option:
              1: Retrieve a password
              2: Add a password
              3: Chage a Password
              4: Remove a password
              5: Change Master Passwordd
              6: Show Service List
              '''
        )