# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.


def iguais(lista1, lista2):
	verdadeiro= True
	falso = False
	print(" Listas  ")
	if (lista1 != lista2):
    		print("iguais: ",falso)
	else:
   			print("iguais: ",verdadeiro)

iguais([1,2,3,4], [5, 6, 7,8])


#2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
def palindrome(p1, p2 ):
	falso = False
	verdadeiro = True
    
	p1 = p1.lower().replace(' ', '')
	p2 = p2.lower().replace(' ', '')
   
    
	print('palindromes perfeitas: ')

	if (p1 == p1[::-1]):
			print('{} = '.format(p1) , falso)	
	else:
			print('{} = '.format(p1) , verdadeiro)

	if (p2 == p2[::-1]):
			print('{} = '.format(p2) , falso)	
	else:
			print('{} = '.format(p2) , verdadeiro)
   


palindrome('Ovo', 'luva')
