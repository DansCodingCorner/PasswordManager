from UI import UI
from scripts import masterPassword
from scripts import hashGenerator
from databaseManager import databaseManager
from scripts import appDriver
import sys

db = databaseManager.databaseManagerInstance
hg = hashGenerator.hashGeneratorInstance
ad = appDriver.appDriverInnstance
mp = masterPassword.masterPasswordInstance
ui = UI.uiInstance

print(f'''
{"="*50}
{"Welcome to the Password Manager!":^50s}
{"="*50}
{"Enter your Master Password:":^50s}
      ''')

masterPasswordEntry = input(">>>")
if mp.checkMatch(masterPasswordEntry):
    ui.printMenu()

