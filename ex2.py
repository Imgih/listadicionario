#Escreva uma função que receba Nome e Idade. Retorne valores que contêm a chave "idade" e cujo valor é maior que 18.
  
lista = {}

def nome():
    return str(input("Digite o seu nome por favor: "))

def idade():
    return int(input("Digite a sua idade por favor: "))

while True:
    Nome = nome()
    if Nome == '':
        break

    Idade = idade()
    lista[Nome] = {
        'Idade': Idade
    }

    for n, i in lista.items():
        if i['Idade'] > 18:
            print('nome:', n ,'idade:', i['Idade'])