#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as MS
from utils import *


bd = MS.connect(host="localhost", user="root", passwd="root") # Instrução de conexão com o MySQL
cursor = bd.cursor()

cursor.execute('DROP DATABASE IF EXISTS financas_db') # Exclui BD se ja existir

print("Criando Banco de Dados...")

sql = '''
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `financas_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `financas_db`.`conta_bancaria` (
    `conbCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `conbBanco` VARCHAR(45) NULL DEFAULT NULL,
    `conbNome` VARCHAR(45) NULL DEFAULT NULL,
    `conbTipo` VARCHAR(45) NULL DEFAULT NULL,
    `conb_usuCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`conbCodigo`),
    INDEX `fk_conta_bancaria_Usuario_idx` (`conb_usuCodigo` ASC),
    CONSTRAINT `fk_conta_bancaria_Usuario`
    FOREIGN KEY (`conb_usuCodigo`)
    REFERENCES `financas_db`.`Usuario` (`usuCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Usuario` (
    `usuCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `usuNome` VARCHAR(45) NULL DEFAULT NULL,
    `usuLogin` VARCHAR(45) NULL DEFAULT NULL,
    `usuSenha` TEXT NULL DEFAULT NULL,
    `usuNumeroDependentes` INT(10) UNSIGNED NULL DEFAULT NULL,
    `usuReceita` FLOAT(11) NULL DEFAULT NULL,
    PRIMARY KEY (`usuCodigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Dependente` (
    `depCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `depNome` VARCHAR(45) NULL DEFAULT NULL,
    `depLogin` VARCHAR(45) NULL DEFAULT NULL,
    `depSenha` TEXT NULL DEFAULT NULL,
    `depReceita` FLOAT(11) NULL DEFAULT NULL,
    `dep_usuCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`depCodigo`),
    INDEX `fk_Dependente_Usuario1_idx` (`dep_usuCodigo` ASC),
    CONSTRAINT `fk_Dependente_Usuario1`
    FOREIGN KEY (`dep_usuCodigo`)
    REFERENCES `financas_db`.`Usuario` (`usuCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Despesa` (
    `desCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `desDescricao` VARCHAR(45) NULL DEFAULT NULL,
    `desValor` FLOAT(11) NULL DEFAULT NULL,
    `desTipo` VARCHAR(45) NULL DEFAULT NULL,
    `des_usuCodigo` INT(11) NOT NULL,
    `des_catCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`desCodigo`),
    INDEX `fk_Despesa_Usuario1_idx` (`des_usuCodigo` ASC),
    INDEX `fk_Despesa_Categoria1_idx` (`des_catCodigo` ASC),
    CONSTRAINT `fk_Despesa_Usuario1`
    FOREIGN KEY (`des_usuCodigo`)
    REFERENCES `financas_db`.`Usuario` (`usuCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_Despesa_Categoria1`
    FOREIGN KEY (`des_catCodigo`)
    REFERENCES `financas_db`.`Categoria` (`catCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Receita` (
    `recCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `recDescricao` VARCHAR(45) NULL DEFAULT NULL,
    `recData` DATE NULL DEFAULT NULL,
    `recValor` FLOAT(11) NULL DEFAULT NULL,
    `recTipo` VARCHAR(45) NULL DEFAULT NULL,
    `rec_usuCodigo` INT(11) NOT NULL,
    `rec_catCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`recCodigo`),
    INDEX `fk_Receita_Usuario1_idx` (`rec_usuCodigo` ASC),
    INDEX `fk_Receita_Categoria1_idx` (`rec_catCodigo` ASC),
    CONSTRAINT `fk_Receita_Usuario1`
    FOREIGN KEY (`rec_usuCodigo`)
    REFERENCES `financas_db`.`Usuario` (`usuCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_Receita_Categoria1`
    FOREIGN KEY (`rec_catCodigo`)
    REFERENCES `financas_db`.`Categoria` (`catCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Categoria` (
    `catCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `catCor` VARCHAR(45) NULL DEFAULT NULL,
    `catNome` VARCHAR(45) NULL DEFAULT NULL,
    PRIMARY KEY (`catCodigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`Sub_Categoria` (
    `subCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `subNome` VARCHAR(45) NULL DEFAULT NULL,
    `sub_catCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`subCodigo`),
    INDEX `fk_Sub_Categoria_Categoria1_idx` (`sub_catCodigo` ASC),
    CONSTRAINT `fk_Sub_Categoria_Categoria1`
    FOREIGN KEY (`sub_catCodigo`)
    REFERENCES `financas_db`.`Categoria` (`catCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;

CREATE TABLE IF NOT EXISTS `financas_db`.`cartao_credito` (
    `creCodigo` INT(11) NOT NULL AUTO_INCREMENT,
    `creBandeira` VARCHAR(45) NULL DEFAULT NULL,
    `creLimite` FLOAT(11) NULL DEFAULT NULL,
    `creDataFechamento` DATE NULL DEFAULT NULL,
    `creNome` VARCHAR(45) NULL DEFAULT NULL,
    `creDataPagamento` DATE NULL DEFAULT NULL,
    `cre_usuCodigo` INT(11) NOT NULL,
    PRIMARY KEY (`creCodigo`),
    INDEX `fk_cartao_credito_Usuario1_idx` (`cre_usuCodigo` ASC),
    CONSTRAINT `fk_cartao_credito_Usuario1`
    FOREIGN KEY (`cre_usuCodigo`)
    REFERENCES `financas_db`.`Usuario` (`usuCodigo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_general_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
'''
cursor.execute(sql) # Instrução de criação do BD
cursor.execute("Use financas_db;") # Seleciona o BD para uso

print("Inserindo dados...")

sql = "insert into Usuario(UsuNome, UsuReceita, UsuLogin, UsuSenha, UsuNumeroDependentes) values ('Bruna Duarte', '300.00', 'bruna123', 'overw1234', 2);"
cursor.execute(sql)
sql = "insert into Usuario(UsuNome, UsuReceita, UsuLogin, UsuSenha, UsuNumeroDependentes) values ('Kimberly Ferreira', '700.00', 'kimberly12','crystal123', 1);"
cursor.execute(sql)
sql = "insert into Usuario(UsuNome, UsuReceita, UsuLogin, UsuSenha, UsuNumeroDependentes) values ('Luiz Eduardo', '200.00', 'LuizMagic30', 'jogo3322', 0);"
cursor.execute(sql)
sql = "insert into conta_bancaria(conbBanco, conbNome, conbTipo, conb_usuCodigo) values ('Banco do Brasil', 'Principal', 'Conta Corrente', 1);"
cursor.execute(sql)
sql = "insert into conta_bancaria(conbBanco, conbNome, conbTipo, conb_usuCodigo) values ('Santander', 'Emergencia', 'Conta Corrente', 2);"
cursor.execute(sql)
sql = "insert into conta_bancaria(conbBanco, conbNome, conbTipo, conb_usuCodigo) values ('Bando do Brasil', 'Principal', 'Conta Corrente', 2);"
cursor.execute(sql)
sql = "insert into cartao_credito(creBandeira, creLimite, creDataPagamento, creDataFechamento, creNome, cre_UsuCodigo) values ('MasterCard', '1000.00', '2018-09-10', '2018-09-20', 'emergencias',1);"
cursor.execute(sql)
sql = "insert into cartao_credito(creBandeira, creLimite, creDataPagamento, creDataFechamento, creNome, cre_UsuCodigo) values ('Elo', '280.00', '2017-11-10', '2017-11-20', 'alimentacao',1);"
cursor.execute(sql)
sql = "insert into cartao_credito(creBandeira, creLimite, creDataPagamento, creDataFechamento, creNome, cre_UsuCodigo) values ('Visa', '3000.00', '2018-10-10', '2018-11-20', 'universitario', 2);"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Vermelho', 'Lazer');"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Azul', 'Alimentação');"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Rosa', 'Transporte');"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Amarelo', 'Escola');"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Preto', 'Faculdade');"
cursor.execute(sql)
sql = "insert into Categoria(catCor, catNome) values ('Roxo', 'Casa');"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, rec_CatCodigo) values ('Auxilio', '2018-03-10', '100.00', 'Mensal', 1, 1);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, Rec_CatCodigo) values ('Auxilio', '2018-01-10', '80.00', 'Mensal', 2, 2);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, Rec_CatCodigo) values ('Economias', '2018-04-29', '200.00', 'Bimestral', 3, 3);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, rec_CatCodigo) values ('Salario', '2018-05-24', '25.00', 'Mensal', 1, 1);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, rec_CatCodigo) values ('Salario', '2018-02-17', '700.00', 'Mensal', 2, 1);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, Rec_CatCodigo) values ('Salario', '2018-01-30', '4350.00', 'Mensal', 3, 2);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, Rec_CatCodigo) values ('Salario', '2018-06-29', '2690.00', 'Mensal', 1, 2);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, rec_CatCodigo) values ('Salario', '2018-05-22', '1500.00', 'Mensal', 2, 1);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, Rec_CatCodigo) values ('Salario', '2018-03-29', '2999.00', 'Mensal', 3, 3);"
cursor.execute(sql)
sql = "insert into Receita(recDescricao, recData, recValor, recTipo, rec_UsuCodigo, rec_CatCodigo) values ('Salario', '2018-03-12', '12800.00', 'Mensal', 1, 1);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Viagem para Bahia', '1500.00', 'Anual', 2, 1);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, Des_CatCodigo) values ('Almoço no IFMG', '1300.00', 'Diario', 3, 2);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Ida para Divinopolis', '100.00', 'Quinzenal', 1, 5);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Agua', '100.00', 'Mensal', 1, 3);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Faculdade', '3000.00', 'Mensal', 1, 2);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, Des_CatCodigo) values ('Plano de Saude', '60.00', 'Anual', 2, 2);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Academia', '100.00', 'Mensal', 2, 3);"
cursor.execute(sql)
sql = "insert into Despesa(desDescricao, desValor, desTipo, des_UsuCodigo, des_CatCodigo) values ('Jogo de basquete', '250.00', 'Mensal', 3, 3);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Supermercado', 2);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Livros', 5);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Viagem', 1);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Material Escolar', 4);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Cozinha', 6);"
cursor.execute(sql)
sql = "insert into Sub_Categoria(subNome, sub_CatCodigo) values ('Limpeza', 6);"
cursor.execute(sql)
sql = "insert into Dependente(depNome, depLogin, depSenha, depReceita, dep_UsuCodigo) values ('Sonia Duarte', 'scDuarte', 'Senha123', 2000.00, 1);"
cursor.execute(sql)
sql = "insert into Dependente(depNome, depLogin, depSenha, depReceita, dep_UsuCodigo) values ('Fatima Faria', 'fatimafaria', 'Senha000', 5000.00, 1);"
cursor.execute(sql)
sql = "insert into Dependente(depNome, depLogin, depSenha, depReceita, dep_UsuCodigo) values ('Aldair Ferreira', 'aldairf', 'Senha284', 150.00, 2);"
cursor.execute(sql)
sql = "insert into Dependente(depNome, depLogin, depSenha, depReceita, dep_UsuCodigo) values ('Joana Rodrigues', 'jrodrigues', 'senha999', 564.00, 3);"
cursor.execute(sql)
sql = "insert into Dependente(depNome, depLogin, depSenha, depReceita, dep_UsuCodigo) values ('Itamar Barbosa', 'itabarbosa', 'senha555', 1452.00, 2);"
cursor.execute(sql)

bd.commit()

continua = True
while (continua):
    print("\n\n==========================================================================")
    print("1- Usuarios, Nome Cartao com data de pagamento vencida")
    print("2- Usuario com receita entre 10/01/2018 e 23/03/2018")
    print("3- Usuario com receita no mês de Março")
    print("4- Somatorio das despesas de cada cliente que possui receita")
    print("5- Numero de cartões de crédito de cada usuario")
    print("6- Numero de dependentes de cada usuario")
    print("7- Numero de tipos de categorias das receita de cada usuario")
    print("8- Numero de tipos de categorias das despesas de cada usuario")
    print("9- Usuarios que possuem mais de 2 contas bancarias")
    print("10- Usuarios que tem receita menor que a soma das receitas de seus dependentes")
    print("11- Usuarios que tenham Receitas maiores 200.00 reais")
    print("12- Usuarios que tenham dependentes com receita maior que 500.00 reais")
    print("13- Usuarios que tenham mais de 3 receitas")
    print("14- Dependentes que tem despesa na sub-categoria Livros")
    print("15- Dependentes que possuem contas no banco do brasil")
    print("16- Usuarios e receita em que receita seja maior que a despesa mensal")
    print("17- Usuarios e limite de crédito em que o maior valor de receita seja abaixo de 1000 ")
    print("18- Usuario e despesa mais cara mensal")
    print("19- Usuario e receita do tipo salario mais barata")
    print("20- Usuario, Receita, Credito e banco do valor de receita mais alto")
    print("2- ")
    print("999999- Sair")
    print("==========================================================================")
    op = input("Opcao: ")
    if (int(op) == 1):
        cursor.execute("select usuNome, creNome from Usuario join cartao_credito where cre_usuCodigo = usuCodigo and creDataPagamento < current_date()")
        cabecalho = ["| Usuario |", "| Cartao de Credito |"]
        gera_relatorio("relatorio_1", cursor, cabecalho)
        print("\nRelatório 1 criado com sucesso!")

    elif(int(op) == 2):
        cursor.execute("select distinct usuNome from Usuario join Receita where rec_usuCodigo = usuCodigo and recData between '2018-01-10' and '2018-03-23';")
        cabecalho = ["| Usuario |"]
        gera_relatorio("relatorio_2", cursor, cabecalho)
        print("\nRelatório 2 criado com sucesso!")

    elif(int(op) == 3):
        cursor.execute("select distinct usuNome from Usuario join Receita where rec_usuCodigo = usuCodigo and MONTH(recData) = '03';")
        cabecalho = ["| Usuario |"]
        gera_relatorio("relatorio_3", cursor, cabecalho)
        print("\nRelatório 3 criado com sucesso!")

    elif(int(op) == 4):
        cursor.execute("select usuNome, sum(desValor) from Usuario join Despesa where usuCodigo = des_usuCodigo group by usuCodigo;")
        cabecalho = ["| Usuario |", "| Receita |"]
        gera_relatorio("relatorio_4", cursor, cabecalho)
        print("\nRelatório 4 criado com sucesso!")

    elif(int(op) == 5):
        cursor.execute("select usuNome, count(creCodigo) from Usuario join cartao_credito where usuCodigo = cre_usuCodigo group by usuCodigo;")
        cabecalho = ["| Usuario |", "| No Cartao |"]
        gera_relatorio("relatorio_5", cursor, cabecalho)
        print("\nRelatório 5 criado com sucesso!")

    elif(int(op) == 6):
        cursor.execute("select  usuNome, count(depCodigo) from Usuario join Dependente  where usuCodigo = dep_usuCodigo group by usuCodigo;")
        cabecalho = ["| Usuario |", "| No Dependente |"]
        gera_relatorio("relatorio_6", cursor, cabecalho)
        print("\nRelatório 6 criado com sucesso!")

    elif(int(op) == 7):
        cursor.execute("select  usuNome, count(catCodigo) from Usuario join Receita join Categoria where usuCodigo = rec_usuCodigo and rec_catCodigo = catCodigo group by usuCodigo;")
        cabecalho = ["| Usuario |", "| Tipos Categorioa Cartao |"]
        gera_relatorio("relatorio_7", cursor, cabecalho)
        print("\nRelatório 7 criado com sucesso!")

    elif(int(op) == 8):
        cursor.execute("select  usuNome, count(catCodigo) from Usuario join Despesa join Categoria  where des_usuCodigo = usuCodigo and des_catCodigo = catCodigo group by usuCodigo;")
        cabecalho = ["| Usuario |", "| Tipos Categoria Despesa |"]
        gera_relatorio("relatorio_8", cursor, cabecalho)
        print("\nRelatório 8 criado com sucesso!")

    elif(int(op) == 9):
        cursor.execute("select usuNome, count(conb_usuCodigo) from Usuario join conta_bancaria where usuCodigo = conb_usuCodigo group by usuCodigo having count(conb_usuCodigo) >= 2;")
        cabecalho = ["| Usuario |", "| No Contas |"]
        gera_relatorio("relatorio_9", cursor, cabecalho)
        print("\nRelatório 9 criado com sucesso!")

    elif(int(op) == 10):
        cursor.execute("select usuNome, usuReceita as receitaUsuario from Usuario join Dependente where usuCodigo = dep_usuCodigo group by usuCodigo having sum(depReceita) > receitaUsuario;")
        cabecalho = ["| Usuario |", "| Receita Usuario |"]
        gera_relatorio("relatorio_10", cursor, cabecalho)
        print("\nRelatório 10 criado com sucesso!")

    elif(int(op) == 11):
        cursor.execute("select usuNome, recValor from Usuario join Receita where usuCodigo = rec_usuCodigo group by usuCodigo having recValor >= 200.00;")
        cabecalho = ["| Usuario |", "| Receita |"]
        gera_relatorio("relatorio_11", cursor, cabecalho)
        print("\nRelatório 11 criado com sucesso!")

    elif(int(op) == 12):
        cursor.execute("select usuNome, depReceita as 'Receita do dependente' from Usuario join Dependente where usuCodigo = dep_usuCodigo group by usuCodigo having depReceita >= 500.00;")
        cabecalho = ["| Usuario |", "| Receita Dependente |"]
        gera_relatorio("relatorio_12", cursor, cabecalho)
        print("\nRelatório 12 criado com sucesso!")

    elif(int(op) == 13):
        cursor.execute("select usuNome, count(recCodigo) from Usuario join Receita where usuCodigo = rec_usuCodigo group by usuCodigo  having count(recCodigo) > 3;")
        cabecalho = ["| Usuario |", "| No Receita |"]
        gera_relatorio("relatorio_13", cursor, cabecalho)
        print("\nRelatório 13 criado com sucesso!")

    elif(int(op) == 14):
        cursor.execute("select depNome from Dependente join Usuario join Despesa join Categoria join (select sub_catCodigo from Sub_Categoria  where subNome = 'Livros' )selescionaSubCat where usuCodigo = dep_usuCodigo and usuCodigo = des_usuCodigo and catCodigo = des_catCodigo and catCodigo = sub_catCodigo;")
        cabecalho = ["| Dependente |"]
        gera_relatorio("relatorio_14", cursor, cabecalho)
        print("\nRelatório 14 criado com sucesso!")

    elif(int(op) == 15):
        cursor.execute("select depNome from Dependente join ( select usuCodigo from Usuario join conta_bancaria where (usuCodigo = conb_usuCodigo and conbBanco = 'Banco do Brasil'))ContaBB where usuCodigo = dep_usuCodigo;")
        cabecalho = ["| Dependente |",]
        gera_relatorio("relatorio_15", cursor, cabecalho)
        print("\nRelatório 15 criado com sucesso!")

    elif(int(op) == 16):
        cursor.execute("SELECT usuNome, sum(recValor) as 'total' FROM Usuario join Receita WHERE recValor > (SELECT sum(desValor) FROM Despesa WHERE desTipo = 'Mensal')")
        cabecalho = ["| Usuario |", "| No Cartao |"]
        gera_relatorio("relatorio_16", cursor, cabecalho)
        print("\nRelatório 16 criado com sucesso!")

    elif(int(op) == 17):
        cursor.execute("SELECT usuNome, creLimite as 'Limite' FROM Usuario join cartao_credito WHERE usuCodigo = cre_usuCodigo and creLimite < (SELECT max(recValor) FROM Receita WHERE recValor < 1000.00)")
        cabecalho = ["| Usuario |", "| Limite |"]
        gera_relatorio("relatorio_17", cursor, cabecalho)
        print("\nRelatório 17 criado com sucesso!")

    elif(int(op) == 18):
        cursor.execute("SELECT usuNome, desDescricao as 'Despesa' FROM Usuario join Despesa WHERE usuCodigo = des_usuCodigo and desValor = (SELECT max(desValor) FROM Despesa WHERE desTipo = 'Mensal')")
        cabecalho = ["| Usuario |", "| Tipo Despesa |"]
        gera_relatorio("relatorio_18", cursor, cabecalho)
        print("\nRelatório 18 criado com sucesso!")

    elif(int(op) == 19):
        cursor.execute("SELECT usuNome, recValor FROM Usuario join Receita WHERE usuCodigo = rec_usuCodigo and recValor = (SELECT min(recValor) FROM Receita WHERE recDescricao = 'Salario') GROUP BY usuCodigo;")
        cabecalho = ["| Usuario |", "| Receita |"]
        gera_relatorio("relatorio_19", cursor, cabecalho)
        print("\nRelatório 19 criado com sucesso!")

    elif(int(op) == 20):
        cursor.execute("SELECT usuNome, recValor, creLimite, conbBanco FROM Usuario join Receita join cartao_credito join conta_bancaria WHERE usuCodigo = rec_usuCodigo and usuCodigo = cre_usuCodigo and usuCodigo = conb_usuCodigo and recValor = (SELECT max(recValor) FROM Receita) GROUP BY usuCodigo;")
        cabecalho = ["| Usuario |", "| Receita |", "| Credito |", "| Banco |"]
        gera_relatorio("relatorio_20", cursor, cabecalho)
        print("\nRelatório 20 criado com sucesso!")
    else:
        continua = False

