valor_inicial = float(input("Digite o valor inicial do investimento: "))
taxa_juros = float(input("Digite a taxa de juros mensal (em %): "))
meses = int(input("Por quantos meses deseja  investir? "))
valor_final = valor_inicial

for mes in range(1, meses):
    valor_final = valor_final + valor_inicial * taxa_juros 
    print(f"No mes {mes}, seu saldo será de R$ {valor_final:.2f}")