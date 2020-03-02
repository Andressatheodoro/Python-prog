# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:58:45 2020

@author: andressa theodoro
"""

'''
aula de  programação pra internet resolução de esercícios:
'''



###
## Exercicios
###

'''
     1) Implemente o metodo define_default_city de acordo com a docstring 
    definida no inicio da funcao. Utilize a clausula else no loop implementado.
'''
import csv
dados = {'id': 21, 'nome': 'Andressa theodoro', 'idade': 19, 'esdado': 
    'São Paulo','courses': ['ADS', 'Redes']}

def define_default_city(estado):
   
    with open('capitais-BR.csv', mode='r', encoding="utf-8") as capitais:
        reader = csv.reader(capitais, delimiter=";")
        for row in reader:
            if estado == row[0]:
                dados['city_origin'] = row[1]
                return True
        else:
            return False
if define_default_city(dados['estado']):
    print(dados['city_origin'])

'''
    2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste
    e teste se sua funcao estah robusta o suficiente.
'''
#ok
'''
     3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de
     CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt.
     Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro.
'''
def cpf():
    cpfs = set()
    with open('cpf.txt','x') as AsCpfs:
        with open('listaCpf.txt', 'y') as cpfsUni:
            for cpf in AsCpfs:
                if cpf not in cpfs:
                    cpfsUni.write(cpf)
                    cpfs.add(cpf)
    return len(cpfs)
print(cpf())