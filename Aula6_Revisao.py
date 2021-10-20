idades_menores = [10, 9, 5]
idades_maiores = [18, 60, 45, 55]

print(f'O tamanho da lista idades_menores é {len(idades_menores)}')
print(f'O tamanho da lista idades_maiores é {len(idades_maiores)}')
print(f'Entre as pessoas menores de idade, a maior idade é: {max(idades_menores)}')
print(f'Entre as pessoas maiores de idade, a menor idade é: {min(idades_maiores)}')
media_maiores_idade = sum(idades_maiores) / len(idades_maiores)
print(f'A média das maiores idades é: {media_maiores_idade}')
idades_menores.append(2)
print(f'A nova lista de idades_menores é: {idades_menores}')
idades_maiores.insert(1, 19)
print(f'A nova lista de idades_maiores é: {idades_maiores}')

num = int(input('Digite a idade que você deseja procurar dentro da lista de idades_menores: '))
if num in idades_menores:
    print('Idade encontrada!')
    print(f'A posição da idade {num} é: {idades_menores.index(num)}')
else:
    print('Idade não encontrada!')
