def calcular_rendimento_composto(valor_inicial: float, taxa_mensal_percentual: float, meses: int) -> list:
    """
    Motor de Cálculo: Processa a evolução do capital mês a mês.
    Retorna uma lista de dicionários contendo o histórico estruturado dos dados.
    """
    taxa_juros = taxa_mensal_percentual / 100
    saldo_atual = valor_inicial
    historico_fluxo_caixa = []

    for mes in range(1, meses + 1):
        rendimento_mes = saldo_atual * taxa_juros
        saldo_atual += rendimento_mes
        
        # Estrutura o registro como se fosse uma linha de banco de dados
        registro_mes = {
            "mes": mes,
            "rendimento_bruto": round(rendimento_mes, 2),
            "saldo_acumulado": round(saldo_atual, 2)
        }
        historico_fluxo_caixa.append(registro_mes)

    return historico_fluxo_caixa


def executar_simulador_investimentos():
    """
    Camada de Interface: Gerencia as entradas do usuário, 
    chama o motor de cálculo e exibe o relatório formatado.
    """
    print('\n---- PIPELINE DE ANÁLISE DE RENDIMENTOS FINANCEIROS ----')
    
    try:
        # Ingestão e tratamento inicial dos dados de entrada
        valor_inicial = float(input('Digite o valor inicial do investimento (R$): '))
        taxa_mensal = float(input('Digite a taxa de juros mensal (em %): '))
        meses = int(input('Por quantos meses deseja projetar? '))

        # Validação das regras de negócio
        if valor_inicial < 0 or taxa_mensal < 0 or meses <= 0:
            print('\033[0;31m[ERRO]\033[m Parâmetros inválidos. Insira valores maiores ou iguais a zero.')
            return

    except ValueError:
        print('\033[0;31m[ERRO CRÍTICO]\033[m Falha na tipagem dos dados. Digite apenas números válidos.')
        return

    # Execução do processamento de dados isolado
    resultado_pipeline = calcular_rendimento_composto(valor_inicial, taxa_mensal, meses)
    
    print('\n---- EVOLUÇÃO MÊS A MÊS ----')
    for registro in resultado_pipeline:
        print(f"Mês {registro['mes']:02d}: "
              f"Saldo acumulado: R$ {registro['saldo_acumulado']:.2f} ︱ "
              f"Rendimento: R$ {registro['rendimento_bruto']:.2f}")

    # Extração das métricas finais para o resumo
    valor_final = resultado_pipeline[-1]["saldo_acumulado"] if resultado_pipeline else valor_inicial
    total_juros_ganhos = valor_final - valor_inicial

    print('\n' + '=' * 50)
    print('              RESUMO METRICAS FINANCEIRAS              ')
    print('=' * 50)
    print(f'Aporte Inicial Analisado: R$ {valor_inicial:.2f}')
    print(f'Total Acumulado em Juros : R$ {total_juros_ganhos:.2f}')
    print(f'Patrimônio Líquido Final: R$ {valor_final:.2f}')
    print('=' * 50)


if __name__ == "__main__":
    executar_simulador_investimentos()