# Escreva uma função que receba itens (números) em um dicionário como entrada e retorne a chave com o maior valor.

lista = {}

def num():
    return str(input('Informe um item: '))

while True:
    item = num()
    if item == '':
        break
    valor = int(input('Informe o valor do item: '))
    lista[item] = valor

maior = max(lista.items())
print('O maior valor da lista: ', maior)