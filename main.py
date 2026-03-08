from UI import UI
from scripts import hashGenerator
from databaseManager import databaseManager
from scripts import appDriver
from scripts import masterPassword
import sys

db = databaseManager.databaseManagerInstance
hg = hashGenerator.hashGeneratorInstance
ui = UI.uiInstance
ad = appDriver.appDriverInnstance
mp = masterPassword.masterPasswordInstance


if not db.isConfigured():
    print("It seems like this is your first time using the password manager, let's get you set up!")
    db.configure()

    ad.changeMasterPassword()

    db.setConfigToTrue()
    print("The password Manager has now been configured, please restart to start storiing passwords!")
    sys.exit()

else:

      print(f'''
{"="*50}
{"Welcome to the Password Manager!":^50s}
{"="*50}''')
      print(f"""
                  .--------.
                / .------. \\
               / /        \\ \\
               | |        | |
              _| |________| |_
            .' |_|        |_| '.
            '._____ ____ _____.'
            |     .'____'.     |
            '.__.'.'    '.'.__.'
            '.__  |      |  __.'
            |   '.'.____.'.'   |
            '.____'.____.'____.'
            '.________________.'
""")
      print(f'''
{"="*50}
{"Enter your Master Password: ":^50s}
{"="*50}''')

      if mp.checkMatch(input()):
          ui.printMenu()
      else:
          print("Incorrect Master Password, exiting...")
          sys.exit()






