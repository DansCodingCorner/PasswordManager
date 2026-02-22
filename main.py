from scripts import masterPassword
from UI import UI
import sys

print(f'''
{"="*50}
{"Welcome to the Password Manager!":^50s}
{"="*50}
{"Enter your Master Password:":^50s}
      ''')
mastterPass = input(">>>")
test = masterPassword.MasterPassword()

if test.checkMatch(mastterPass):
    ui = UI.UIManager()
    ui.printMenu()
else:
    print("Invalid Password")
    sys.exit()