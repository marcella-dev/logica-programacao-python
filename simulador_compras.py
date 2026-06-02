def processar_fluxo_compras() -> None:
    """
    Simula uma esteira de checkout de PDV (Ponto de Venda).
    Realiza o tratamento de strings e a agregação dos valores em tempo real.
    """
    VALOR_PADRAO_ZERADO = 0.0
    total_acumulado = VALOR_PADRAO_ZERADO
    contador_itens = 0

    print("=== CAIXA REGISTRADORA ===")
    print("Diretriz: Digite o valor do produto ou 'sair' para finalizar o lote.\n")

    while True:
        entrada_usuario = input("Digite o valor do produto (R$): ").strip()

        if entrada_usuario.lower() == 'sair':
            break

        try:
            # Substitui vírgula por ponto (caso o usuário digite no padrão BR "10,50")
            entrada_higienizada = entrada_usuario.replace(",", ".")
            
            # Conversão e tipagem dos dados
            valor_produto = float(entrada_higienizada)

            if valor_produto < 0:
                print("[AVISO] Valores negativos não são permitidos para processamento de itens.")
                continue

            total_acumulado += valor_produto
            contador_itens += 1
            print(f"-> Item {contador_itens:02d} processado com sucesso. Subtotal: R$ {total_acumulado:.2f}")

        except ValueError:
            # Captura dados corrompidos sem derrubar a aplicação
            print(f"[ERRO DE INGESTÃO] Entrada inválida: '{entrada_usuario}'. Digite apenas números.")

    print("\n" + "=" * 45)
    print("          CONSOLIDAÇÃO DO LOTE (NF-e)        ")
    print("=" * 45)
    print(f"Quantidade total de itens: {contador_itens} unidades")
    print(f"Valor total agregado     : R$ {total_acumulado:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    processar_fluxo_compras()
