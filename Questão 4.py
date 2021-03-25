'''
4 - Escreva uma função que faça a verificação de existência de um item em uma
lista. A função deve retornar o tamanho da lista caso o item não exista ou o próprio
item caso ele exista.
'''
numeros = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]

item_digitado =int(input("Digite um número para procurar\n"))


def verifica_item(numeros, item_digitado):
    if item_digitado in numeros:
        print (f'Encontramos o seu número procurado: {item_digitado}')
    else:
        não_tem = len(numeros)
        print(f'Sinto muito, não encontramos seu número nos {não_tem} itens.')
    

verifica_item(numeros, item_digitado)