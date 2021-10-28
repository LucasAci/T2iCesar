# Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1- Domingo, 2- Segunda, etc.). Exibir mensagem “Valor Inválido”
# caso um número inesperado for informado.

diaDaSemana = int(input("Informe um número de 1 a 7, para saber qual dia da semana ele representa: "))

if diaDaSemana == 1:
    print("Domingo")
elif diaDaSemana == 2:
    print("Segunda")
elif diaDaSemana == 3:
    print("Terça")
elif diaDaSemana == 4:
    print("Quarta")
elif diaDaSemana == 5:
    print("Quinta")
elif diaDaSemana == 6:
    print("Sexta")
elif diaDaSemana == 7:
    print("Sábado")
else:
    print("Valor inválido.")








