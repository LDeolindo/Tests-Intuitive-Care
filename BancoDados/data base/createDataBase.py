import mysql.connector
import config

dbName = 'mydatabase'

db = mysql.connector.connect(
  host = config.host,
  user = config.user,
  password = config.password,
)

def useDataBase(mycursor):
  try:
    mycursor.execute("USE {}".format(dbName))
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Using database {}.".format(dbName))

def createDataBase(mycursor):
  try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'".format(dbName))
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Database {} created successfully!".format(dbName))
    useDataBase(mycursor)

if __name__ == '__main__':
  mycursor = db.cursor()
  createDataBase(mycursor)
  mycursor.close()
  db.close()