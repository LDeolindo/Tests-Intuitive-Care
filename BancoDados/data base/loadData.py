import os
import mysql.connector
# importa as tabelas criadas
import tablesDictionary
# importa as configurações
import config
# importa o banco criado
import createDataBase

dbName = createDataBase.dbName

# tenta fazer a conexão com o banco
try:
  db = mysql.connector.connect(
    host = config.host,
    user = config.user,
    password = config.password,
    database = dbName
  )
except mysql.connector.Error as err:
  print(err)

# carrega os dados para a tabela relatorio cadop
def loadDataFromRelat(name, mycursor, path, table):
  try:
    print("Loading: {}".format(table))
    # query para o carregamento dos dados
    query = """LOAD DATA INFILE '{}' 
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
            `Cargo Representante`, @var1)
            SET `Data Registro ANS` = STR_TO_DATE(@var1, '%d/%m/%Y')
            ;
            """.format(path,table)
    mycursor.execute(query)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Loaded successfully!")

# carrega os dados para as tabelas de demonstracoes_contabeis
def loadData(fileName, mycursor):
  for name in fileName:
    # caminho onde estão os dados
    path = '/var/lib/dados/{}'.format(name)
    # nome das tabelas que estao na pasta
    table = name.split(".")[0]
    if name == 'Relatorio_cadop.csv': loadDataFromRelat(name, mycursor, path, table)
    else:
      try:
        print("Loading: {}".format(table))
        # query para o carregamento dos dados
        query = """LOAD DATA INFILE '{}' IGNORE
                INTO TABLE {} 
                CHARACTER SET Latin1 
                FIELDS TERMINATED BY ';' 
                OPTIONALLY ENCLOSED BY '"' 
                LINES TERMINATED BY '\r\n' 
                IGNORE 1 LINES 
                (@DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, @VL_SALDO_FINAL)
                SET DATA = STR_TO_DATE(@DATA, '%d/%m/%Y'),
                VL_SALDO_FINAL = REPLACE(@"VL_SALDO_FINAL", ",", ".")
                ;
                """.format(path,table)
        mycursor.execute(query)
      except mysql.connector.Error as err:
        print(err)
      else:
        print("Loaded successfully!")

if __name__ == '__main__':
  # pasta onde estão os dados para pegar os nomes das tabelas
  fileName = os.listdir('./dados/.')
  mycursor = db.cursor()
  loadData(fileName, mycursor)
  db.commit()
  mycursor.close()
  db.close()