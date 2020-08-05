import mysql.connector
# importo as suas configurações
import config

# nome do banco de dados
dbName = 'mydatabase'

# faz a conexão com o banco
db = mysql.connector.connect(
  host = config.host,
  user = config.user,
  password = config.password,
)

# função utilizar o banco
def useDataBase(mycursor):
  try:
    mycursor.execute("USE {}".format(dbName))
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Using database {}.".format(dbName))

# função criar o banco
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