import sqlite3


class  DatabaseManager:




    def connectToDb(self):
       connection = sqlite3.connect('data/test.db')

       return connection

    def createCursor(self, connection):

        cursor = connection.cursor()

        return cursor
    
    def closeConnection(self,  connection):

        connection.close()

    def setMasterPassword(self):


        self.cursor.execute()

    def addPasswordToDatabase():
        pass

    def removePasswordFromDatabase():
        pass

    def changePassword():
       pass

    def defRetrievePassword():
        pass

    def createTable(self):
        connection = self.connectToDb()
        cursor = self.createCursor(connection)

        create_table_query = '''
CREATE TABLE IF NOT EXISTS MasterPassword (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    salt TEXT NOT NULL,
    masterPasswordHash  TEXT NOT NULL
);
'''
        cursor.execute(create_table_query)
        connection.commit()

        connection.close()

        

    def showTables():
        pass

    
    
db = DatabaseManager()
db.createTable()