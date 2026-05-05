dolar = 4.93
euro = 5.76

valor_real = float(input('Digite o valor em R$: '))
print('''Escolha em qual moeda quer converter:
      1 - Dólar
      2 - Euro''')
moeda_escolhida = (input(' Sua opção: ')).strip()

if moeda_escolhida == '1':
    total = valor_real / dolar
    print(f'Com R${valor_real:.2f} você pode comprar US${total:.2f}.')
elif moeda_escolhida == '2':
    total = valor_real / euro
    print(f'Com R${valor_real:.2f} você pode comprar {total:.2f}€.')   
else:
    print('Opção inválida!')
