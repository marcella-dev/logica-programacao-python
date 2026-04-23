valor_casa = float(input('Qual o valor do imóvel que você deseja comprar? '))
salario = float(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos deseja terminar de pagar o imóvel? '))
prestacao = valor_casa / (anos * 12)
if prestacao > salario * 0.30:
    print('Infelizmente o empréstimo foi NEGADO.')
else:
    print(f'A prestação mensal será de R${prestacao:.2f} reais em {anos} anos.')
