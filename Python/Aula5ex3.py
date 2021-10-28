# Faça um programa que peça5 notas e armazene-as em uma lista.
# Por fim, exiba todas as notas.

notas = []
QUANT = 5

for i in range(QUANT):
    notas.append(float(input("Digite uma nota: ")))

media = sum(notas) / len(notas)

print(f'As notas informadas foram: {notas}')
print(f"A média das notas é: {media}")