def processar_checkout_loja() -> None:
    """
    Motor de Regras de Negócio: Processa o checkout de vendas aplicando 
    políticas dinâmicas de descontos e juros com base na forma de pagamento.
    """
    DESCONTO_DINHEIRO = 0.10  # 10% off
    DESCONTO_DEBITO = 0.05    # 5% off
    JUROS_PARCELADO_LONGO = 0.20  # 20% de juros
    
    print("<>" * 25)
    print(f"{'LOJAS M&M':^45}")
    print("<>" * 25)

    try:
        # Ingestão e higienização do dado financeiro
        entrada_preco = input('Qual foi o preço total das compras? R$ ').strip().replace(",", ".")
        preco_base = float(entrada_preco)

        if preco_base <= 0:
            print("[ALERTA] O valor da transação deve ser maior que zero.")
            return

    except ValueError:
        print("[ERRO CRÍTICO] Valor monetário inválido. Transação abortada.")
        return

    print("\nFORMAS DE PAGAMENTO DISPONÍVEIS")
    print("1 - À vista (Dinheiro / Cheque)   [-10% Desconto]")
    print("2 - À vista (Cartão de Débito)    [-5% Desconto]")
    print("3 - Parcelado em 2x (Cartão)      [Preço de Etiqueta]")
    print("4 - Parcelado em 3x (Cartão)      [+20% Juros de Financiamento]")

    try:
        opcao = int(input('\nSelecione o ID da condição de pagamento: '))
    except ValueError:
        print("[ERRO CRÍTICO] ID da opção inválido. Use apenas números inteiros.")
        return

    if opcao == 1:
        valor_final = preco_base * (1 - DESCONTO_DINHEIRO)
        print(f"-> Condição aplicada: À vista com {DESCONTO_DINHEIRO*100:.0f}% de desconto.")
        
    elif opcao == 2:
        valor_final = preco_base * (1 - DESCONTO_DEBITO)
        print(f"-> Condição aplicada: Débito com {DESCONTO_DEBITO*100:.0f}% de desconto.")
        
    elif opcao == 3:
        valor_final = preco_base
        parcela = valor_final / 2
        print(f"-> Condição aplicada: Parcelamento 2x sem juros.")
        print(f"   Detalhamento: 2 parcelas mensais fixas de R$ {parcela:.2f}")
        
    elif opcao == 4:
        valor_final = preco_base * (1 + JUROS_PARCELADO_LONGO)
        parcela = valor_final / 3
        print(f"-> Condição aplicada: Parcelamento 3x com incidência de juros.")
        print(f"   Detalhamento: 3 parcelas mensais fixas de R$ {parcela:.2f}")
        
    else:
        print(f"[ERRO OPERACIONAL] Código de opção '{opcao}' inexistente no portfólio de pagamentos.")
        return

    print("\n" + "═" * 45)
    print("               CONSOLIDADO DA VENDA          ")
    print("═" * 45)
    print(f"Subtotal Bruto     : R$ {preco_base:.2f}")
    print(f"Totalizador Líquido: R$ {valor_final:.2f}")
    print("═" * 45)


if __name__ == "__main__":
    processar_checkout_loja()