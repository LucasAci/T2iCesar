# Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa
# e mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado).
# Mostre uma mensagem de erro, se necessário
civil = input("Informe o seu estado civil: S | C | V | D: ")

if civil == "S":
    print(f"Solteiro")
elif civil == "C":
    print(f"Casado")
elif civil == "V":
    print(f"Viúvo")
elif civil == "D":
    print(f"Divorciado")
else:
    print(f"Você não informou corretamente. Insira as letras  S | C | V | D ")

