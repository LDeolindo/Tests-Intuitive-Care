import datetime
import mysql.connector
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

# query para: Quais as 10 operadoras que mais tiveram despesas com 
# "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" 
# no último trimestre?
def queryQ4(mycursor):
  try:
    print("Searching : ")
    query = """
            SELECT `Razão Social`, `Registro ANS`
            FROM Relatorio_cadop as REL, 
              ( SELECT REG_ANS, DESCRICAO, SUM(VL_SALDO_FINAL) as SALDO
                FROM 1T2020
                WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                GROUP BY REG_ANS
                ORDER BY SALDO DESC LIMIT 10
              ) as DESP
            WHERE REL.`Registro ANS` = DESP.REG_ANS;
            """
    mycursor.execute(query)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("As 10 operadoras que mais tiveram despesas  no último trimestre (1T - 2020):")
    for (i, j) in mycursor:
      print(" {} - {}".format(i, j))

# query para: Quais as 10 operadoras que mais tiveram despesas com 
# "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" 
# no último ano?
def queryPastYear(mycursor):
  try:
    print("Searching : ")
    query = """
            SELECT `Razão Social`, `Registro ANS`
            FROM Relatorio_cadop as R, 
              ( SELECT REG_ANS, DESCRICAO, SUM(VL_SALDO_FINAL) as SALDO
                FROM (
                      SELECT REG_ANS, DESCRICAO, VL_SALDO_FINAL FROM 1T2019
                        UNION ALL
                      SELECT REG_ANS, DESCRICAO, VL_SALDO_FINAL FROM 2T2019
                        UNION ALL
                      SELECT REG_ANS, DESCRICAO, VL_SALDO_FINAL FROM 3T2019
                        UNION ALL
                      SELECT REG_ANS, DESCRICAO, VL_SALDO_FINAL FROM 4T2019
                      ) T
                WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
                GROUP BY REG_ANS
                ORDER BY SALDO DESC LIMIT 10
                ) as F
            WHERE R.`Registro ANS` = F.REG_ANS;
            """
    mycursor.execute(query)
  except mysql.connector.Error as err:
    print(err)
  else:
    print("As 10 operadoras que mais tiveram despesas no último ano (2019):")
    for (i, j) in mycursor:
      print(" {} - {}".format(i, j))

if __name__ == '__main__':
  mycursor = db.cursor()
  queryQ4(mycursor)
  queryPastYear(mycursor)
  mycursor.close()
  db.close()