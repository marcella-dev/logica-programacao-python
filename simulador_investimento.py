def simular_juros_composto():

    print('\n---- SIMULADOR DE RENDIMENTOS ----')
    valor_inicial = float(input('Digite o valor inicial do investimento: '))
    taxa_mensal = float(input('Digite a taxa de juros mensal (em %): '))
    meses = int(input('Por quantos meses deseja investir? '))

    if valor_inicial < 0 or taxa_mensal < 0 or meses <= 0:
        print('[ERRO] Por favor, insira valores válidos maiores que zero.')
        return
    taxa_juros = taxa_mensal / 100
    valor_final = valor_inicial
     
    print('\n---- EVOLUÇÃO MÊS A MÊS ----')
    for mes in range(1, meses + 1):
        juros_do_mes = valor_final * taxa_juros
        valor_final += juros_do_mes
        print(f'Mês {mes:02d}: Saldo acumulado de R$ {valor_final:.2f} ︱ Rendimento: R$ {juros_do_mes:.2f}')

    total_juros_ganhos = valor_final - valor_inicial
    print('\n' + '=' * 40)
    print('        RESUMO DA ANÁLISE        ')
    print('=' * 40)
    print(f'Valor inicial aplicado: R$ {valor_inicial:.2f}')
    print(f'Total ganho em juros: R$ {total_juros_ganhos:.2f}')
    print(f'Resultado bruto final: R$ {valor_final:.2f}')
    print('=' * 40)

if __name__ == "__main__":
    simular_juros_composto()
      