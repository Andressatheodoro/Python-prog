# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 18:56:11 2020

@author: andressa theodoro
"""

'''
aula de  programação pra internet resolução de esercícios:
'''



'''
	DESAFIO!!!
	Implemente um algoritmo para inverter a ordem de uma string em sua
	linguagem de programacao favorita. Nao use funcoes/metodos prontos
'''

# Exercicios


# 1) Extraia o titulo do livro da string
book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

titulo = book1[0:10]  
print (titulo)
titulo2 = book2[0:12]  
print (titulo2)
titulo3 = book3[0:19]  
print (titulo3)

print("\n \n")
# 2) Salve o titulo de cada livro em uma variável

titulo1 = book1.split('by')
titulo2 = book2.split('by')
titulo3 = book3.split('by')

# 3) Quantos caracteres cada título tem?
tamanhoTitulo = len(book1)
print(tamanhoTitulo)
tamanhoTitulo = len(book2)
print(tamanhoTitulo)
tamanhoTitulo = len(book3)
print(tamanhoTitulo)
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}
titulo = book1[0:10] 
autor = book1[12:30]
ano = book1[32:36] 
print("           livro 1")
print (" titulo: ",titulo +"\n autor: ",autor +"\n ano:  ",ano)
print("       \n    livro 2")
titulo2 = book2[0:12] 
autor2 = book2[12:36]
ano2 = book2[37:42]  
print (" Titulo:",titulo2 +"\n Autor:", autor2 +"\n Ano:",ano2)
print("     \n      livro 3")
titulo3 = book3[0:19] 
autor3 = book3[23:45]
ano3 = book3[46:51]  
print (" Titulo:",titulo3 +"\n Autor:", autor3 +"\n Ano:",ano3)

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_generico = str(input("Digite uma palavra: ")).lower().replace(' ', '')

palindrome_one = 'ovo'.lower().replace(' ', '')
palindrome_two = 'Natan'.lower().replace(' ', '')
palindrome_three = 'luz azul'.lower().replace(' ', '')
palindrome_four = 'caneta azul'.lower().replace(' ', '')


if (palindrome_generico == palindrome_generico[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_generico))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_generico))

if (palindrome_one == palindrome_one[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_one))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_one))

if (palindrome_two == palindrome_two[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_two))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_two))

if (palindrome_three == palindrome_three[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_three))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_three))		

if (palindrome_four == palindrome_four[::-1]):
	print('{} é um Palindrome perfeito'.format(palindrome_four))	
else:
	print('{} não é um palindrome perfeito'.format(palindrome_four))	



