# Montar uma query analítica que traga a resposta para as seguintes perguntas:
#   - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
#   - Quais as 10 operadoras que mais tiveram despesas com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último ano?

# searchByGoal = (status) => {
#     const goalsFiltered = this.state.goals.filter((item) => moment(item.year).format('YYYY') === this.state.yearSearch.format('YYYY') && item.goals.map(e => e.status).includes(status));

#     this.setState({ goalsFiltered, status });
#   }

# SELECT REG_ANS
# FROM 4T2019
# GROUP BY DESCRICAO = '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' or 
# 		DESCRICAO = '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' OR 
#         DESCRICAO = '%EVENTOS / SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR' OR
#         DESCRICAO = '%EVENTOS /SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR';

import datetime
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

def query(mycursor, text):
  try:
    print("Searching : ")
    query = """
            SELECT operadoras count(*)==10
            FROM 1T2019, 2T2019, 3T2019, 4T2019, Relatorio_cadop
            WHERE DESCRICAO = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR';
            """
    mycursor.execute(query, (dateStart, dateEnd))
  except mysql.connector.Error as err:
    print(err)
  else:
    print("Loaded successfully!")

if __name__ == '__main__':
  mycursor = db.cursor()
  text = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
  query(mycursor, text)
  mycursor.close()
  db.close()