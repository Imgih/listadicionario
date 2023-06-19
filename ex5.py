#Escreva uma função que receba um dicionário como entrada e retorna uma nova lista contendo apenas as chaves

dicionario = {'Baleia':'mamifero', 'tubarao':'peixe', 'Pinguin': 'Ave' }

def chaves(dicionario):
    chaves = dicionario.keys()
    print(chaves)

chaves(dicionario)