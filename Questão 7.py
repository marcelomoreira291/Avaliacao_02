'''
7- Utilizando List Comprehension crie uma lista de listas
'''

numeros_a = [x for x in range(0, 20)] 
numeros_b = [x for x in range (21, 40)] 

nova_lista_numeros = list(numeros_a + numeros_b) 
print(f'A nova lista que foi gerada: {nova_lista_numeros}')
