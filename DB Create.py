import pymysql
databaseServerIP = "127.0.0.1" 
databaseUserName = "root"
databaseUserPassword = ""
newDatabaseName = "LibraryDB"
charSet = "utf8mb4" 

cusrorType = pymysql.cursors.DictCursor

connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,charset=charSet,cursorclass=cusrorType)

try:
    cursorInsatnce        = connectionInstance.cursor()                                    

    sqlStatement            = "CREATE DATABASE "+newDatabaseName  

    cursorInsatnce.execute(sqlStatement)
    
except Exception as e:

    print("Exeception occured:{}".format(e))

finally:
    connectionInstance.close()
