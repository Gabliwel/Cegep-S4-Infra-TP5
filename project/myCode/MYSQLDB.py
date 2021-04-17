import mysql.connector
from myCode import EnvironmentVariable


def getConfig():
    config = {
        'user':EnvironmentVariable.getEnvironmentVariable('INFRA_TP5_DB_USER'),
        'password': EnvironmentVariable.getEnvironmentVariable('INFRA_TP5_DB_PASSWORD'),
        'host': EnvironmentVariable.getEnvironmentVariable('INFRA_TP5_DB_HOST'),
        'port': EnvironmentVariable.getEnvironmentVariable('INFRA_TP5_DB_PORT'),
        'database':'usersDB'}
    return config


class MYSQLDB():
    __instance = None
    
    @staticmethod
    def getInstance():
        if MYSQLDB.__instance == None:
            MYSQLDB()
        return MYSQLDB.__instance
 
    
    def __init__(self):
        if MYSQLDB.__instance != None:
            raise Exception("There should only be one instance of SQLiteDB")
        else:
            MYSQLDB.__instance = self
            #self.db = mysql.connector.connect(**getConfig())
            
    def getUsersOfType(self, type):
        #TODO validate that type is either 0 or 1
        conn = mysql.connector.connect(**getConfig())
        cursor = conn.cursor()
        query = "SELECT username FROM users WHERE isInitialUser = " + str(type)
        cursor.execute(query)
        users = []
        for (username,) in cursor:
            users.append(username)
        cursor.close()
        conn.close()
        return users
    
    def runUpdateQuery(self, query):
        try:
            conn = mysql.connector.connect(**getConfig())
            cursor = conn.cursor()
            print(query, flush=True)
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True) #TODO do something better here
        finally:
            cursor.close()
            conn.close()      
    
    
