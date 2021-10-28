# Informe o nome, idade e altura de 3 pessoas. Após inserir as informações,
# busque pelo nome de um usuário. Se ele existir no sistema, exiba suas
# informações. Caso contrário, exiba a seguinte mensagem:
# "Usuário não encontrado!".

PESSOAS = 3
nomes = []
idades = []
alturas = []

# Inserindo valores nas listas
for i in range(PESSOAS):
    nomes.append(input('Digite um nome: '))
    idades.append(int(input('Digite uma idade: ')))
    alturas.append(float(input('Digite uma altura: ')))

# Buscando por um usuário
pessoa = input('Digite o nome da pessoa que você deseja encontrar: ')

if pessoa in nomes:
    posicao = nomes.index(pessoa)
    print(f'Nome: {nomes[posicao]} Idade: {idades[posicao]} Altura: {alturas[posicao]}')
else:
    print('Usuário não encontrado!')
