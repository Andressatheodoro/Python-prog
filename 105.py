# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:58:41 2020

@author: andressa theodoro
"""

'''
aula de  programação pra internet resolução de esercícios:
'''

'''
	DESAFIO!!!
	1) Crie uma lista com os 1000 primeiros numeros pares. Não use loop!
    
	2) Crie uma lista com os numeros de 0 ate 99999999999999999999999999.
    Depois crie um loop para percorrer a lista ateh encontrar o primeiro multiplo de 5.
	OBS.: Use sua linguagem de programacao favorita. Nao use funcoes/metodos prontos.
'''





# Exercicios

# 1) Faca um loop para retornar: ['A','B','C']
lista= []
lista= ['a','b','c']
i=1
while (i <= 10):
	print(lista)
	i += 1
	
## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
def soma(lista):
    l = lista
    return l

l = soma([1,2,3,4,5])
soma = 0
for i in range(len(l)):
    soma += l[i]
print("soma dos elementos",soma)



    
# 3) Faca um loop para retornar apenas os numeros impares

def impares(lista):
	for i in lista:
		if(i%2 == 1):
			print("impar:",i)
	
impares([0, 1, 3, 4, 5])		
		   
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
def string(frase):
	cont = 0
	frase = frase.replace(',', ' ').split(' ')
	for ver in frase:
		if(len(ver)>= 5):
			cont += 1 
	return cont
print("quantidade de palavra de tamanho 5:")
print(string( 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100
def multiplos(lista):
	multiplos3 = [x for x in lista if x % 3 == 0] 
	print("multiplos de 3:",multiplos3)
multiplos(list(range(3,100)))

# 6)Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
def primos(listaP):
	primo = []
	for x in listaP:
		cont = 0				
		for y in range(1 , x+1):
			if(x%y == 0):
				cont+= 1
		if(cont <= 2):
			primo.append(x)	
	print("numeros primos:",primo)
primos(list(range(2,10)))




