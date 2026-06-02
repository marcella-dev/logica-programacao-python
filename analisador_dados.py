def calcular_metricas_analiticas(lista_dados: list) -> dict:
    """
    Motor de Agregação: Processa coleções numéricas brutas e extrai
    indicadores estatísticos consolidados para governança e BI.
    """
    if not lista_dados:
        return {}

    quantidade = len(lista_dados)
    soma_total = sum(lista_dados)
    maior_valor = max(lista_dados)
    menor_valor = min(lista_dados)
    media_calculada = soma_total / quantidade

    # Retorna o sumário de dados perfeitamente estruturado
    return {
        "volume_transacoes": quantidade,
        "soma_total_agregada": round(soma_total, 2),
        "media_valores": round(media_calculada, 2),
        "valor_maximo_registrado": round(maior_valor, 2),
        "valor_minimo_registrado": round(menor_valor, 2)
    }


def executar_pipeline_analytics():
    """
    Camada de Ingestão: Coleta e higieniza fluxos de dados do terminal,
    gerencia erros de tipagem e dispara o motor analítico.
    """
    dados_brutos = []
    
    print("<>" * 23)
    print(f"{'PIPELINE DE DATA PROFILING & AGGREGATION':^45}")
    print("<>" * 23)
    print("Diretriz: Insira valores numéricos no lote. Digite 0 para encerrar.\n")

    while True:
        try:
            entrada_usuario = input('Digite o valor numérico: ').strip().replace(",", ".")
            valor = float(entrada_usuario)
            
            if valor == 0:
                break
                
            dados_brutos.append(valor)
            
        except ValueError:
            print(f"[ERRO DE INGESTÃO] Entrada inválida: '{entrada_usuario}'. Registro ignorado.")
            continue

    # Aciona a camada de processamento de dados isolada
    sumario_performance = calcular_metricas_analiticas(dados_brutos)

    if sumario_performance:
        print("\n" + "═" * 45)
        print(f"{'CONSOLIDADO COMPREENSIVO DE METRICAS':^45}")
        print("═" * 45)
        print(f"Volume Total de Transações: {sumario_performance['volume_transacoes']} registros")
        print(f"Faturamento Total Agregado: R$ {sumario_performance['soma_total_agregada']:.2f}")
        print(f"Média Ponderada do Lote  : R$ {sumario_performance['media_valores']:.2f}")
        print(f"Pico de Valor Coletado   : R$ {sumario_performance['valor_maximo_registrado']:.2f}")
        print(f"Vale de Valor Coletado   : R$ {sumario_performance['valor_minimo_registrado']:.2f}")
        print("═" * 45)
    else:
        print('\n[AVISO] Nenhum registro válido foi coletado para processamento.')


if __name__ == "__main__":
    executar_pipeline_analytics()