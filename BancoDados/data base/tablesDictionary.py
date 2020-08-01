TABLES = {}

TABLES['Relatorio_cadop'] = (
    "CREATE TABLE `Relatorio_cadop` ("
    "  `Registro ANS` int(6) NOT NULL,"
    "  `CNPJ` int(14) NOT NULL,"
    "  `Razão Social` varchar(150) NOT NULL,"
    "  `Nome Fantasia` varchar(150),"
    "  `Modalidade` varchar(100) NOT NULL,"
    "  `Logradouro` varchar(100) NOT NULL,"
    "  `Número` int(4) NOT NULL,"
    "  `Complemento` varchar(100) NOT NULL,"
    "  `Bairro` varchar(100) NOT NULL,"
    "  `Cidade` varchar(50) NOT NULL,"
    "  `UF` char(2) NOT NULL,"
    "  `CEP` int(9) NOT NULL,"
    "  `DDD` int(3) NOT NULL,"
    "  `Telefone` int(9) NOT NULL,"
    "  `Fax` int(9) NOT NULL,"
    "  `Endereço eletrônico` varchar(100) NOT NULL,"
    "  `Representante` varchar(100) NOT NULL,"
    "  `Cargo Representante` varchar(50) NOT NULL,"
    "  `Data Registro ANS` date NOT NULL,"
    "   PRIMARY KEY (`Registro ANS`)"
    ")")

TABLES['1T2018'] = (
    "CREATE TABLE `1T2018` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['2T2018'] = (
    "CREATE TABLE `2T2018` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['3T2018'] = (
    "CREATE TABLE `3T2018` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['4T2018'] = (
    "CREATE TABLE `4T2018` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['1T2019'] = (
    "CREATE TABLE `1T2019` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['2T2019'] = (
    "CREATE TABLE `2T2019` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['3T2019'] = (
    "CREATE TABLE `3T2019` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")

TABLES['4T2019'] = (
    "CREATE TABLE `4T2019` ("
    "  id INT NOT NULL AUTO_INCREMENT,"
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(150) NOT NULL,"
    "  `VL_SALDO_FINAL` REAL NOT NULL,"
    "  `Registro ANS Relatorio` int(6) NOT NULL,"
    "   PRIMARY KEY (id),"
    "   FOREIGN KEY (`Registro ANS Relatorio`) REFERENCES Relatorio_cadop(`Registro ANS`) ON DELETE NO ACTION"
    ")")