# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:56:09 2020

@author: andressa theodoro
"""

'''
aula de  programação pra internet resolução de esercícios:
'''
list = ['a', 1, 3.14159265359]
print("list:",list)
print('\n')

RED = "\033[1;30;41m]"

print('\n\n\n')
weekdays = ['mon','tues','wed','thurs','fri']
print('\033[1;31m lista inicial: \033[m')
print(weekdays)

# Como selecionar 'wed' pelo indice?
day = weekdays[2]
print('\n')    
print('\033[1;31m Selecionando wed \033[m')
print('dia :',day)

# Como verificar o tipo de 'mon'?
print("\n")  
print(type(weekdays[0]))

# Como separar 'wed' até 'fri'?
print("\n3")
print(weekdays[2:5])

# Quais as maneiras de selecionar 'fri' por indice?
print("\n")  
print(weekdays[4])
print(weekdays[4:5])

# Qual eh o tamanho dos dias e days_list?
print('\n5')
dias = len(day)
lista= len(weekdays)
print('tamanho de dias: ', dias)
print('tamanho de days_list: ', lista)

# Como inverter a ordem dos dias?
print('\n')
print('Dias invertidos  \033[m')
print('lista alual:',weekdays[::-1])


# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1,'zero')
print(list)

# Como limpar list?
list.clear()
print('\n')
print(' Limpar lista  \033[m')
print('lista alual:',list)

# Como deletar list?

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento 
# e remove-lo de list?
print('\n 10')
ultimo_elemento = list[-1]
print(ultimo_elemento)
list.remove(list[-1])
print(list)
