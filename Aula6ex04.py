# Ler a idade de 4 pessoas, calcular e informar a média;
# Exibir:
# As idades que são superiores a média das idades.
# A quantidade de idades que são inferiores a média das idades.

idades = []
quantidade = 0
for i in range(4):
    idades.append(float(input("Digite a idade: ")))

media = sum(idades) / len(idades)
print(f"A média das idades é: {media}\n")

print("As idades superiores a média são: ")
for i in range(4):
    if idades[i] > media:
        print(idades[i])

    else:
        quantidade += 1
print(f"A quantidade de idades inferiores a média : {quantidade}")



