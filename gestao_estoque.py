estoque = { 
    'Notebook': {'quantidade': 10, 'preço': 3500.00}, 
    'Mouse': {'quantidade': 50, 'preço': 89.90}, 
    'Teclado': {'quantidade': 15, 'preço': 250.00},
    'Monitor': {'quantidade': 8, 'preço': 1250.75}
}

def exibir_estoque():
    print("\n--- ESTOQUE ATUAL ---")
    for produto, dados in estoque.items():
        print(f"Produto: {produto} | Quantidade: {dados['quantidade']} | Preço: R${dados['preço']:.2f}")

def registrar_entrada():
    print("\n--- REGISTRAR ENTRADA ---")
    nome_produto = input("Digite o nome do produto: ").strip().title()
    
    if nome_produto not in estoque:
        print(f"Erro: O produto '{nome_produto}' não foi cadastrado.")
        return # Sai da função imediatamente
        
    quantidade = int(input(f"Quantidade a adicionar para {nome_produto}: "))
    if quantidade > 0:
        estoque[nome_produto]['quantidade'] += quantidade
        print(f"Sucesso! Novo estoque de {nome_produto}: {estoque[nome_produto]['quantidade']}")
    else:
        print("[ERRO] A quantidade de entrada deve ser maior que zero.")

def registrar_saida():
    print("\n--- REGISTRAR SAÍDA ---")
    nome_produto = input("Digite o nome do produto: ").strip().title()
    
    if nome_produto not in estoque:
        print(f"Erro: O produto '{nome_produto}' não foi encontrado.")
        return

    quantidade = int(input(f"Quantidade para saída de {nome_produto}: "))
    if quantidade <= 0:
        print("[ERRO] A quantidade de saída deve ser maior que zero.")
        return

    if estoque[nome_produto]['quantidade'] >= quantidade:
        estoque[nome_produto]['quantidade'] -= quantidade
        print(f"Saída registrada! Novo estoque de {nome_produto}: {estoque[nome_produto]['quantidade']}")
    else:
        print(f"Erro: Estoque insuficiente. Saldo atual: {estoque[nome_produto]['quantidade']}")

while True:
    print("\n--- SISTEMA DE GESTÃO DE ESTOQUE - DataCode Solutions ---")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    
    opcao = input("\nEscolha uma opção (1-4): ").strip()

    if opcao == "1":
        exibir_estoque()
    elif opcao == "2":
        registrar_entrada()
    elif opcao == "3":
        registrar_saida()
    elif opcao == "4":
        print("\nEncerrando o sistema da DataCode Solutions... Até logo!")
        break
    else:
        print(f"\n[ERRO] A opção '{opcao}' é inválida. Por favor, escolha um número de 1 a 4.")