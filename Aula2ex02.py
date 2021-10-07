# Faça um algoritmo que receba o ano de nascimento do usuário,
# o ano atual, e imprima a idade.

AnoNascimento = int(input("Digite o ano de nascimento: "))
AnoAtual = int(input("Digite o ano atual: "))
idade = AnoAtual - AnoNascimento

print(f"A idade é: {idade}anos.")
