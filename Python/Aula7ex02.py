# Faça um programa que solicite o peso e altura de 3 pessoas.
# Calcule o IMC de cada pessoa e armazene-os em uma lista.
# Calcule a média do IMC das três pessoas.
# Imprima:
# a lista de IMCs
# a média dos IMCs
# os IMCs acima da média

imc = []

for i in range(3):
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    imcAtual = peso / (altura*altura)
    imc.append(imcAtual)

mediaImc = sum(imc) / len(imc)

print(f"Todos os IMCs: {imc}")
print(f"Média dos IMCs: {mediaImc}")
print("IMCs acima da média: ")

for i in range(len(imc)):
    if imc[i] > mediaImc:
        print(imc[i])


