import os
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

def loadDataFromRelat(name, mycursor, path, table):
  try:
    print("Loading: ")
    query = """LOAD DATA INFILE '{}' IGNORE
            INTO TABLE {} 
            CHARACTER SET Latin1 
            FIELDS TERMINATED BY ';' 
            OPTIONALLY ENCLOSED BY '"' 
            LINES TERMINATED BY '\r\n' 
            IGNORE 3 LINES 
            (`Registro ANS`, CNPJ, `Razão Social`,
            `Nome Fantasia`, Modalidade, Logradouro,
            Número, Complemento, Bairro, Cidade,
            UF, CEP, DDD, Telefone, Fax,
            `Endereço eletrônico`, Representante,
            `Cargo Representante`, @`Data Registro ANS`)
            SET `Data Registro ANS` = STR_TO_DATE(@'`Data Registro ANS`', '%m/%d/%Y');
            """.format(path,table)
    mycursor.execute(query)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Loaded successfully!")

def loadData(fileName, mycursor):
  for name in fileName:
    path = '/var/lib/dados/{}'.format(name)
    table = name.split(".")[0]
    if name == 'Relatorio_cadop.csv': loadDataFromRelat(name, mycursor, path, table)
    else:
      try:
        print("Loading: {}".format(table))
        query = """LOAD DATA INFILE '{}' IGNORE
                INTO TABLE {} 
                CHARACTER SET Latin1 
                FIELDS TERMINATED BY ';' 
                OPTIONALLY ENCLOSED BY '"' 
                LINES TERMINATED BY '\r\n' 
                IGNORE 1 LINES 
                (@DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_FINAL)
                SET DATA = STR_TO_DATE(@DATA, '%m/%d/%Y'),
                VL_SALDO_FINAL = REPLACE(@"VL_SALDO_FINAL", ",", ".")
                ;
                """.format(path,table)
        mycursor.execute(query)
      except mysql.connector.Error as err:
        print(err)
      else:
        print("Loaded successfully!")

if __name__ == '__main__':
  fileName = os.listdir('./dados/.')
  mycursor = db.cursor()
  loadData(fileName, mycursor)
  db.commit()
  mycursor.close()
  db.close()