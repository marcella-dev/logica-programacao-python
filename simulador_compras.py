total = 0 

while True:
    valor = input("Qual o valor do produto? ou (Digite 'sair' para encerrar): ")
    if valor.lower() == 'sair':
        break
    valor = float(valor)
    total += valor
print("O total da compra é: R$", total)
