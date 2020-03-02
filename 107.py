# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:58:48 2020

@author: andressa theodoro
"""

'''
aula de  programação pra internet resolução de esercícios:
'''

###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
list = [2, 3, 5, 7, 11, 13, 17, 19]
tuple = (2, 3, 5, 7, 11, 13, 17, 19)
print(list)
print(tuple)
mostrarLista = dir(list)
mostrarTupla = dir(tuple)
print(mostrarLista)
print(mostrarTupla)
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
def diferenca(x, y):
    print("Métodos únicos de uma lista: ", set(x) - set(y))
    print("Métodos únicos de uma tupla: ", set(y) - set(x))
diferenca(mostrarLista, mostrarTupla)
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor3 = dict(id=28, name='Jorge Armino', idade=37, state_origin='Rio Grande do Sul', courses=['Filosofia', 'Informática e Sociedade'] )

professor1['coordenadas'] = 0,0
professor2['coordenadas'] = 0,0
professor3['coordenadas'] = 0,0