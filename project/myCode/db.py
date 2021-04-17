from myCode import SQLiteDB
from myCode import MYSQLDB
from myCode import EnvironmentVariable

def getDB():
    dbType = EnvironmentVariable.getEnvironmentVariable("INFRA_TP5_DB_TYPE")
    if dbType == "SQLite":
        return SQLiteDB.SQLiteDB.getInstance()
    elif dbType == "MYSQL":
        return MYSQLDB.MYSQLDB.getInstance() 
    else:
        raise Exception("Unsupported dbtype for environment variable (INFRA_TP5_DB_TYPE). Received (" + dbType + "), we support only SQLite and MYSQl")
     
def getInitialUsersFromDB():
    return getDB().getUsersOfType(1)
    
def getNewUsersFromDB():
    return getDB().getUsersOfType(0)

def delUserFromDB(username):
    query = "DELETE FROM users WHERE username = \'" + username + "\'"
    getDB().runUpdateQuery(query)
    
def addUserToDB(username):
    query = "INSERT INTO users (username) VALUES (\'" + username + "\')"
    getDB().runUpdateQuery(query)
