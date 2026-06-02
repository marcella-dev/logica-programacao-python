def criar_estado_inicial_estoque() -> dict:
    """
    Simula a carga inicial de dados vinda de um banco de dados.
    """
    return { 
        'Notebook': {'quantidade': 10, 'preço': 3500.00}, 
        'Mouse': {'quantidade': 50, 'preço': 89.90}, 
        'Teclado': {'quantidade': 15, 'preço': 250.00},
        'Monitor': {'quantidade': 8, 'preço': 1250.75}
    }


def exibir_estoque(estoque: dict) -> None:
    """Consolida e apresenta os dados estruturados do inventário."""
    print("\n--- ESTOQUE ATUAL ---")
    for produto, dados in estoque.items():
        print(f"Produto: {produto:<10} | Quantidade: {dados['quantidade']:02d} | Preço Unitário: R$ {dados['preço']:.2f}")


def registrar_entrada(estoque: dict) -> None:
    """Processa a entrada de insumos e atualiza o estado do inventário."""
    print("\n--- REGISTRAR ENTRADA ---")
    nome_produto = input("Digite o nome do produto: ").strip().title()
    
    if nome_produto not in estoque:
        print(f"[ERRO] O produto '{nome_produto}' não consta na base de dados.")
        return 
        
    try:
        quantidade = int(input(f"Quantidade a adicionar para {nome_produto}: "))
        if quantidade > 0:
            estoque[nome_produto]['quantidade'] += quantidade
            print(f"[SUCESSO] Atualização concluída. Novo saldo de {nome_produto}: {estoque[nome_produto]['quantidade']} unidades.")
        else:
            print("[ERRO] A quantidade de entrada deve ser estritamente maior que zero.")
    except ValueError:
        print("[ERRO CRÍTICO] Entrada de dados inválida. A quantidade deve ser um número inteiro.")


def registrar_saida(estoque: dict) -> None:
    """Processa a baixa de insumos avaliando as regras de consistência de saldo."""
    print("\n--- REGISTRAR SAÍDA ---")
    nome_produto = input("Digite o nome do produto: ").strip().title()
    
    if nome_produto not in estoque:
        print(f"[ERRO] O produto '{nome_produto}' não foi localizado.")
        return

    try:
        quantidade = int(input(f"Quantidade para saída de {nome_produto}: "))
        if quantidade <= 0:
            print("[ERRO] A quantidade de saída deve ser estritamente maior que zero.")
            return

        # Validação de consistência do banco de dados (evitar estoque negativo)
        if estoque[nome_produto]['quantidade'] >= quantidade:
            estoque[nome_produto]['quantidade'] -= quantidade
            print(f"[SUCESSO] Baixa concluída. Novo saldo de {nome_produto}: {estoque[nome_produto]['quantidade']} unidades.")
        else:
            print(f"[ALERTA] Estoque insuficiente para a transação. Saldo atual: {estoque[nome_produto]['quantidade']} unidades.")
    except ValueError:
        print("[ERRO CRÍTICO] Entrada de dados inválida. A quantidade deve ser um número inteiro.")


def calcular_valor_total_inventario(estoque: dict) -> float:
    """Algoritmo de agregação de dados para gerar métricas de valor patrimonial."""
    return sum(dados['quantidade'] * dados['preço'] for dados in estoque.values())


def inicializar_sistema_datacode():
    """Gerenciador de fluxo principal da aplicação (Orquestrador)."""
    estoque_data = criar_estado_inicial_estoque()

    while True:
        print("\n" + "=" * 55)
        print("    SISTEMA DE GESTÃO DE ESTOQUE - DataCode Solutions    ")
        print("=" * 55)
        print("1 - Visualizar Estoque Atual")
        print("2 - Registrar Entrada de Produto")
        print("3 - Registrar Saída de Produto")
        print("4 - Encerrar Lote e Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ").strip()

        if opcao == "1":
            exibir_estoque(estoque_data)
        elif opcao == "2":
            registrar_entrada(estoque_data)
        elif opcao == "3":
            registrar_saida(estoque_data)
        elif opcao == "4":
            valor_patrimonial = calcular_valor_total_inventario(estoque_data)
            print("\n" + "═" * 55)
            print("         CONSOLIDAÇÃO DE ENCERRAMENTO DATACODE       ")
            print("═" * 55)
            print(f"Valor Total do Ativo em Estoque: R$ {valor_patrimonial:.2f}")
            print("Auditoria finalizada com sucesso. Desconectando sistema...")
            print("═" * 55 + "\n")
            break
        else:
            print(f"\n[ERRO] A opção '{opcao}' é inválida. Selecione um ID operacional de 1 a 4.")


if __name__ == "__main__":
    inicializar_sistema_datacode()