import sqlite3

class SQLiteDB():
    __instance = None
    
    @staticmethod
    def getInstance():
        if SQLiteDB.__instance == None:
            SQLiteDB()
        return SQLiteDB.__instance
 
    
    def __init__(self):
        if SQLiteDB.__instance != None:
            raise Exception("There should only be one instance of SQLiteDB")
        else:
            SQLiteDB.__instance = self
            self.db = sqlite3.connect(":memory:", check_same_thread=False)
            #Populating DB with fake data
            query = "CREATE TABLE users (username VARCHAR(32) NOT NULL, isInitialUser BIT DEFAULT 0 NOT NULL, UNIQUE(username));"
            self.runUpdateQuery(query)
            query = "INSERT INTO users (username, isInitialUser) VALUES (\"Bob\", 1);"
            self.runUpdateQuery(query)
            query = "INSERT INTO users (username, isInitialUser) VALUES (\"Bill\", 0);"
            self.runUpdateQuery(query)
            query = "INSERT INTO users (username, isInitialUser) VALUES (\"Body\", 1);"
            self.runUpdateQuery(query)
            query = "INSERT INTO users (username, isInitialUser) VALUES (\"Joe\", 0);"
            self.runUpdateQuery(query)
            query = "INSERT INTO users (username, isInitialUser) VALUES (\"Jack\", 0);"
            self.runUpdateQuery(query)

    def getUsersOfType(self, type):
        #TODO validate that type is either 0 or 1
        cursor = self.db.cursor()
        query = "SELECT username FROM users WHERE isInitialUser = " + str(type)
        cursor.execute(query)
        users = []
        for (username,) in cursor:
            users.append(username)
        cursor.close()
        return users
    
    def runUpdateQuery(self, query):
        try:
            cursor = self.db.cursor()
            print(query, flush=True)
            cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True) #TODO do something better here
        finally:
            cursor.close()      
    
