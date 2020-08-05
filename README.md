# Tests-Intuitive-Care

Testes realizados para o processo seletivo IntuitiveCare.

## Teste 1 - WebScraping

### Pré Requisitos
Para o desenvolvimento foi utilizado a linguagem [Python](https://www.python.org/) com as bibliotecas:
* [Requests](https://requests.readthedocs.io/en/master/);
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/);

### Começando
Primeiramente, abra o terminal no diretório do teste e instale as dependências:
* `$ pip install requests`
* `$ pip install beautifulsoup4`
* `$ pip install lxml`

### Executando
Para rodar a aplicação use o comando:
`$ python webScp.py`

Logo após a execução gerará na pasta do teste um arquivo**.pdf**

## Teste 3 - Banco de dados

### Pré Requisitos
Para o desenvolvimento foi utilizado a linguagem [Python](https://www.python.org/) com as bibliotecas:
* [mysql.connector](https://dev.mysql.com/doc/connector-python/en/);

E também foi utilizado o Banco de Dados Mysql:
* **./data base/config.py** - Contém as configurações do Banco de Dados, altere com as suas:

### Começando
Primeiramente, abra o terminal no diretório do teste e instale as dependências:
* `$ pip install mysql-connector-python`

### Configurando Banco de Dados
Dentro do diretório tem a pasta **./data base/**, onde estão contidos os arquivo de inicialização e carregamento dos dados:

#### Para cria o Banco de Dados
`$ python "/data base/createDataBase.py"`

#### Para cria as Tabelas
`$ python "/data base/createTable.py"`

#### Para carregar os Dados
`$ python "/data base/loadData.py"`

### Executando
Para rodar a aplicação use o comando:
`$ python "/data base/queries.py"`



