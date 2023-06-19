#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista com as chaves ordenadas em ordem alfabética.
dicionario = {'Baleia':'mamifero', 'tubarao':'peixe', 'Pinguin': 'Ave' }

def chaves(dicionario):
    ordem = sorted(dicionario.keys())
    ordenacao = [(chave, dicionario[chave]) for chave in ordem]
    print(ordenacao)


chaves(dicionario)
