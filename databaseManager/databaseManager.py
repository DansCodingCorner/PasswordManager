import sqlite3

class  DatabaseManager:


    def connectToDb(self):
       connection = sqlite3.connect('data/test.db')

       return connection



    def setMasterPassword(self, salt, masterPasswordHash):

        salt = str(salt)
        masterPasswordHash = str(masterPasswordHash)

        connection = self.connectToDb()
        cursor =  connection.cursor()
        clearTableQuery = '''DELETE FROM  MasterPassword;'''

        cursor.execute(clearTableQuery)

        cursor.execute(
        "INSERT INTO MasterPassword (salt, masterPasswordHash) VALUES (?, ?)",
        (salt, masterPasswordHash)
    )

        connection.commit()
        connection.close()



    def addPasswordToDatabase(self, serviceName, username, passwordHash):
        connection = self.connectToDb()
        cursor =  connection.cursor()

        cursor.execute(f'''INSERT INTO MasterPassword
VALUES({serviceName},{username},{passwordHash})''')
        
        connection.commit()
        connection.close()


    def removePasswordFromDatabase():
        pass


    def changePassword():
       pass


    def defRetrievePassword():
        pass


    def createTable(self):

        connection = self.connectToDb()
        cursor = connection.cursor()

        create_masterPassword_table_query = '''
CREATE TABLE IF NOT EXISTS MasterPassword (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salt TEXT NOT NULL,
    masterPasswordHash  TEXT NOT NULL
);
'''

        cursor.execute(create_masterPassword_table_query)

        create_Password_table_query = '''
CREATE TABLE IF NOT EXISTS Password (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    serviceName TEXT NOT NULL,
    username TEXT NOT NULL,
    passwordHash  TEXT NOT NULL
);
'''
        cursor.execute(create_Password_table_query)

        connection.commit()

        connection.close()

    def dropTale(self, tableName):

        connection = self.connectToDb()
        cursor = connection.cursor()

        dropTablequery = tableName

        cursor.execute(dropTablequery)

        connection.commit()
        connection.close()

    def showTables():
        pass

    
    
db = DatabaseManager()
db.setMasterPassword( "SALT", "HASH")