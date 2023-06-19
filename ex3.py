#Escreva uma função que receba duas listas de mesmo comprimento, uma contendo chaves e outra contendo valores, e retorna um dicionário criado a partir dessas listas.

frutas = ['maça', 'abacate', 'limao', 'tangerina']
precos = [3.90, 9.00, 2.99, 3.00]
quantnome = len(frutas)

for i in range(quantnome):
    print(f'{frutas[i]}, {precos[i]}')