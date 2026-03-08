import sqlite3
import base64

class  DatabaseManager:


    def connectToDb(self):
       connection = sqlite3.connect('data/test.db')

       return connection


    def setMasterPassword(self, salt, masterPasswordHash):

        connection = self.connectToDb()
        cursor =  connection.cursor()
        clearTableQuery = '''DELETE FROM  MasterPassword;'''

        cursor.execute(clearTableQuery)

        cursor.execute(
    "INSERT INTO MasterPassword (salt, masterPasswordHash) VALUES (?, ?)",
    (salt, masterPasswordHash)   
)

        selecttHashQuery = '''SELECT * FROM MasterPassword'''

        cursor.execute(selecttHashQuery)
        hash = cursor.fetchall()
        print(hash)

        connection.commit()
        connection.close()



    def retieveMasterPasswordSalt(self):
        conn = self.connectToDb()
        cursor = conn.cursor()
        cursor.execute("SELECT salt FROM MasterPassword LIMIT 1")
        row = cursor.fetchone()
        conn.close()
        if row:
            return row[0]        

    def retrieveMasterPasswordHash(self):

        connection = self.connectToDb()
        cursor =  connection.cursor()

        selecttHashQuery = '''SELECT masterPasswordHash FROM MasterPassword'''

        cursor.execute(selecttHashQuery)
        hash = cursor.fetchone()
        hash = hash[0]
        
        return hash


    def addPasswordToDatabase(self, serviceName, username, passwordHash):
        connection = self.connectToDb()
        cursor =  connection.cursor()

        cursor.execute("INSERT INTO Password (serviceName, username, passwordHash) VALUES (?, ?, ?)",
    (serviceName, username, passwordHash))
        
        connection.commit()
        connection.close()

    def retrievePasswoordHashFromDB(self, serviceName):
        connection = self.connectToDb()
        cursor = connection.cursor()

        cursor.execute(
    "SELECT passwordHash FROM Password WHERE serviceName = ?",
    (serviceName,)
    )       
        passwordHash = cursor.fetchone()
        passwordHash = passwordHash[0]

        return passwordHash


    def removePasswordFromDatabase(self, serviceName):
        connection = self.connectToDb()
        cursor =  connection.cursor()

        cursor.execute("DELETE FROM Password WHERE serviceName = ?",(serviceName,))

    def changePassword(self, serviceName, passwordHash):
       connection = self.connectToDb()
       cursor = connection.cursor()
       
       cursor.execute(
    "UPDATE Password SET passwordHash = ? WHERE serviceName = ?",
    (passwordHash, serviceName)
)
       connection.commit()
       connection.close()


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

        cursor.execute("DROP TABLE ?",(tableName,))

        connection.commit()
        connection.close()


databaseManagerInstance = DatabaseManager()

