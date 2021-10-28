# Uma empresa deseja reavaliar os salários dos seus funcionários.
# Será reajustado o salário daqueles que estão há 2 anos ou mais sem receber aumento.
# O ajuste acontecerá da seguinte forma:
# Funcionário com mais de 10 anos de casa, 30%.
# Funcionário que tem entre 5 a 10 anos de casa, 20%.
# Funcionário com menos de 5 anos de casa, 10%.
# Aqueles que receberam aumento salarial há menos de 2 anos não estão aptos ao reajuste salarial coletivo.

# Faça um programa que receba as seguintes informações sobre o funcionário:
# Ano de admissão, salário atual, ano do último reajuste salarial
# O programa deverá mostrar o novo salário do funcionário ou uma mensagem informando
# que ele não está apto ao reajuste salarial coletivo.

# Constante
ANO_ATUAL = 2021

# Entrada de dados do funcionário
ano_admissao = int(input("Digite o no de admissão: "))
salario_atual = float(input("Digite o salario atual: "))
ano_reajuste = int(input("Digite o ano do ultimo reajuste salarial: "))

# Cálculo do tempo do último reajuste
tempo_reajuste = ANO_ATUAL - ano_reajuste

# Cálculo do tempo de casa
tempo_casa = ANO_ATUAL - ano_admissao

if tempo_reajuste >= 2:
    if tempo_casa > 10:
        novo_salario = salario_atual + (salario_atual * 0.3)
    elif 5 <= tempo_casa <= 10:
        novo_salario = salario_atual + (salario_atual * 0.2)
    else:
        novo_salario = salario_atual + (salario_atual * 0.1)

    print(f"Seu novo salário é {novo_salario}")  # o print tem q está dentro do if

else:
    print("Você não está apto ao reajuste salarial coletivo.")
