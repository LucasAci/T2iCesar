# Faça um programa que leia um nome de usuário e a sua senha.
# A regra do programa é que a senha não seja igual ao nome do usuário.
# Caso seja igual, o sistema apresenta uma mensagem de erro
# e volta a solicitar a senha, caso seja diferente
# o programa finaliza com uma mensagem de cadastro efetuado.

nome = input("Informe seu nome de usuário: ")
senha = input("Informe a sua senha: ")

while nome == senha:
    print("Erro! A senha deve ser diferente do nome do usuário.")
    senha = input("Informe a senha: ")
print("Cadastro efetuado.")
