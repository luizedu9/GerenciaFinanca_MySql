#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import pyexcel_ods3 as pods
import subprocess

def gera_relatorio(arquivo, cursor, cabecalho):
    dicionario = {}
    lista = []
    #subprocess.call("clear", shell=True)
    print("Gerando PDF. Aguarde...")
    lista.append(cabecalho)
    temp = []
    for i in range(0, len(cabecalho)):
    	temp.append(" ")
    lista.append(temp)
    for row in cursor.fetchall():
        temp = []
        for x in range(0, len(row)):
            temp.append(str(row[x]))
        lista.append(temp)
    dicionario['Relatorio'] = lista
    pods.save_data(arquivo + ".ods", dicionario)
    print("\n")
    subprocess.call("soffice --headless --convert-to pdf *.ods", shell=True)
    subprocess.call("rm *.ods", shell=True)
