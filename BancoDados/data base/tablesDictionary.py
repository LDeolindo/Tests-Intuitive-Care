TABLES = {}

TABLES['Relatorio_cadop'] = (
    "CREATE TABLE `Relatorio_cadop` ("
    "  `Registro ANS` int(6) NOT NULL,"
    "  `CNPJ` bigint(15) NOT NULL,"
    "  `Razão Social` varchar(255) NOT NULL,"
    "  `Nome Fantasia` varchar(255) NOT NULL,"
    "  `Modalidade` varchar(100) NOT NULL,"
    "  `Logradouro` varchar(100) NOT NULL,"
    "  `Número` varchar(20) NOT NULL,"
    "  `Complemento` varchar(100) NOT NULL,"
    "  `Bairro` varchar(100) NOT NULL,"
    "  `Cidade` varchar(50) NOT NULL,"
    "  `UF` char(2) NOT NULL,"
    "  `CEP` varchar(10) NOT NULL,"
    "  `DDD` char(4) NOT NULL,"
    "  `Telefone` varchar(50) NOT NULL,"
    "  `Fax` varchar(50) NOT NULL,"
    "  `Endereço eletrônico` varchar(100) NOT NULL,"
    "  `Representante` varchar(100) NOT NULL,"
    "  `Cargo Representante` varchar(50) NOT NULL,"
    "  `Data Registro ANS` date NOT NULL,"
    "   PRIMARY KEY (`Registro ANS`)"
    ")")

TABLES['1T2018'] = (
    "CREATE TABLE `1T2018` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['2T2018'] = (
    "CREATE TABLE `2T2018` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['3T2018'] = (
    "CREATE TABLE `3T2018` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['4T2018'] = (
    "CREATE TABLE `4T2018` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['1T2019'] = (
    "CREATE TABLE `1T2019` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['2T2019'] = (
    "CREATE TABLE `2T2019` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['3T2019'] = (
    "CREATE TABLE `3T2019` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['4T2019'] = (
    "CREATE TABLE `4T2019` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")

TABLES['1T2020'] = (
    "CREATE TABLE `1T2020` ("
    "  `DATA` date NOT NULL,"
    "  `REG_ANS` int(6) NOT NULL,"
    "  `CD_CONTA_CONTABIL` int(9) NOT NULL,"
    "  `DESCRICAO` varchar(250) NOT NULL,"
    "  `VL_SALDO_FINAL` DECIMAL(13,2) NOT NULL"
    ")")