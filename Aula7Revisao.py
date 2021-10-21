# Inserir o nome de 5 pessoas em uma lista
# e exibi-los na ordem inversa.

nomes = []
for i in range(5):
    nomes.append(input('Digite o nome: '))

nomes.reverse()
print(f'Nomes com ordem invertida: {nomes}')

# Agora, exiba os nomes em ordem alfabética

nomes.sort()
print(f"Nomes em ordem alfabética: {nomes}")

# Exiba um nome por linha

for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")