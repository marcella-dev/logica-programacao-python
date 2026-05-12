dados = []
while True:
    valor = float(input('Digite o valor ou 0 para sair: '))
    if valor == 0:
        break
    dados.append(valor)
if len(dados) > 0:
    quantidade = len(dados)
    soma_total = sum(dados)
    maior_valor = max(dados)
    menor_valor = min(dados)
    media = soma_total / quantidade

    print('\n' + '<>' * 17)
    print('      RELATÓRIO DE ANALYTICS     ')
    print('<>' * 17)
    print(f'Total de transações: {quantidade}')
    print(f'Soma total: R${soma_total:.2f}')
    print(f'Média dos valores: R${media:.2f}')
    print(f'Maior valor coletado: R${maior_valor:.2f}')
    print(f'Menor valor coletado: R${menor_valor:.2f}')
    print('<>' * 17)
else:
    print('Nenhum dado foi coletado.')