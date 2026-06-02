def analisar_risco_credito(valor_imovel: float, salario_comprovado: float, anos_pagamento: int) -> dict:
    """
    Motor de Risco: Analisa a viabilidade de concessão de crédito imobiliário
    com base na regra de ouro de governança bancária (limite de 30% da renda).
    Retorna um payload estruturado com o veredito e métricas.
    """
    MARGEM_CONSIGNAVEL_PERMITIDA = 0.30
    meses_financiamento = anos_pagamento * 12
    
    # Cálculo da parcela e da capacidade máxima de pagamento do cliente
    parcela_mensal = valor_imovel / meses_financiamento
    limite_maximo_parcela = salario_comprovado * MARGEM_CONSIGNAVEL_PERMITIDA
    
    # Tomada de decisão baseada nas regras de risco
    aprovado = parcela_mensal <= limite_maximo_parcela
    comprometimento_renda_percentual = (parcela_mensal / salario_comprovado) * 100

    # Retorna o resultado estruturado (mimetiza um registro de banco de dados/JSON)
    return {
        "status_concessao": "APROVADO" if aprovado else "NEGADO",
        "valor_parcela": round(parcela_mensal, 2),
        "limite_permitido": round(limite_maximo_parcela, 2),
        "comprometimento_renda_ %": round(comprometimento_renda_percentual, 1),
        "meses_contrato": meses_financiamento
    }


def executar_pipeline_credito():
    """
    Camada de Ingestão e Interface: Captura os dados do proponente,
    valida os tipos e dispara o motor de análise de risco.
    """
    print("<>" * 30)
    print(f"{'SISTEMA DE ANÁLISE DE RISCO - CONCESSÃO DE CRÉDITO':^55}")
    print("<>" * 30)

    try:
        # Captura e higienização inicial dos dados
        valor_casa = float(input('Valor do imóvel desejado (R$): ').strip().replace(",", "."))
        salario = float(input('Valor do salário líquido comprovado (R$): ').strip().replace(",", "."))
        anos = int(input('Prazo de amortização em anos: ').strip())

        # Validação das restrições matemáticas e de negócios
        if valor_casa <= 0 or salario <= 0:
            print("[ALERTA] Valores financeiros devem ser estritamente maiores que zero.")
            return
        if anos <= 0:
            print("[ALERTA] O prazo em anos deve ser maior que zero (evita divisão por zero).")
            return

    except ValueError:
        print("[ERRO CRÍTICO] Falha na validação dos tipos de dados inseridos.")
        return

    # Execução do motor de risco de dados
    resultado_analise = analisar_risco_credito(valor_casa, salario, anos)

    # Exibição analítica do veredito (Simula o painel de um analista de crédito)
    print("\n" + "═" * 55)
    print("               PAINEL DE AUDITORIA DE CRÉDITO        ")
    print("═" * 55)
    print(f"Status da Solicitação     : {resultado_analise['status_concessao']}")
    print(f"Valor da Parcela Projetada: R$ {resultado_analise['valor_parcela']:.2f}")
    print(f"Margem Máxima Permitida   : R$ {resultado_analise['limite_permitido']:.2f}")
    print(f"Comprometimento de Renda  : {resultado_analise['comprometimento_renda_ %']}%")
    print(f"Duração do Contrato       : {resultado_analise['meses_contrato']} meses")
    print("═" * 55)


if __name__ == "__main__":
    executar_pipeline_credito()
