nomes = ['Joyce', 'Paulo', 'Cecilia']
idades = [32, 30, 29]
alturas = [1.66, 1.79, 1.68]

NOME = 'Paulo'

if NOME in nomes:
    posicao = nomes.index(NOME)
    print(f'Nome: {nomes[posicao]} Idade: {idades[posicao]} Altura: {alturas[posicao]}')
