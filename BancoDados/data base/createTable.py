import mysql.connector
import tablesDictionary
import config
import createDataBase

dbName = createDataBase.dbName

try:
  db = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.password,
    database = dbName
  )
except mysql.connector.Error as err:
  print(err)

def createTable(mycursor, table, tableName):
  try:
    mycursor.execute(table)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Table {} created successfully!".format(tableName))

if __name__ == '__main__':
  mycursor = db.cursor()
  for table in tablesDictionary.TABLES:
    tab = tablesDictionary.TABLES[table]
    createTable(mycursor, tab, table)
  mycursor.close()
  db.close()