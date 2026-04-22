senha_mestra = "1234"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_mestra:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta! Tente novamente.")