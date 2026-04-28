print('<>' * 21)
print('{:^40}'.format('LOJAS M&M'))
print('<>' * 21)
preco = float(input('Qual foi o preço total das compras? R$'))
print('''FORMAS DE PAGAMENTO:
1 - à vista dinheiro/cheque
2 - à vista cartão
3 - 2x no cartão
4 - 3x no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 0.10)
elif opcao == 2:
    total = preco - (preco * 0.05)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS ')
elif opcao == 4:
    total = preco + (preco * 0.20)
    parcela = total / 3
    print(f'Sua compra será parcelada em 3x de R${parcela:.2f} COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento! Tente novamente.')
print(f'Sua compra de {preco:.2f} vai custar {total:.2f} no final.')
