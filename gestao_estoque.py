estoque = { 
    'Notebook': {'quantidade': 10, 'preço': 3500.00}, 
    'Mouse': {'quantidade': 50, 'preço': 89.90}, 
    'Teclado': {'quantidade': 15, 'preço': 250.00},
    'Monitor gamer': {'quantidade': 25, 'preço': 1250.75}
    }

while True:
    print("\n--- SISTEMA DE GESTÃO DE ESTOQUE - DataCode Solutions ---")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair do Sistema")
    
    opcao = input("\nEscolha uma opção (1-4): ")

    if opcao == "1":
        print("\n--- ESTOQUE ATUAL ---")
        # Iterando sobre o dicionário para mostrar cada produto e seus detalhes
        for produto, dados in estoque.items():
            print(f"Produto: {produto} | Quantidade: {dados['quantidade']} | Preço: R${dados['preço']:.2f}")
    elif opcao == "2":
        print("\n--- REGISTRAR ENTRADA ---")
        nome_produto = input("Digite o nome do produto: ").capitalize()
    
        # Verificando se o produto existe no dicionário
        if nome_produto in estoque:
            quantidade_entrada = int(input(f"Quantidade a adicionar para {nome_produto}: "))
            # Atualização aritmética acumulativa
            estoque[nome_produto]['quantidade'] += quantidade_entrada
            print(f"Sucesso! Novo estoque de {nome_produto}: {estoque[nome_produto]['quantidade']}")
        else:
            print(f"Erro: O produto '{nome_produto}' não foi encontrado.")

    elif opcao == "3":
        print("\n--- REGISTRAR SAÍDA ---")
        nome_produto = input("Digite o nome do produto: ").capitalize()
    
        # 1ª Validação: O produto existe?
        if nome_produto in estoque:
            quantidade_saida = int(input(f"Quantidade para saída de {nome_produto}: "))
        
            # 2ª Validação: Existe saldo suficiente?
            if estoque[nome_produto]['quantidade'] >= quantidade_saida:
                # Atribuição subtrativa
                estoque[nome_produto]['quantidade'] -= quantidade_saida
                print(f"Saída registrada! Novo estoque de {nome_produto}: {estoque[nome_produto]['quantidade']}")
            else:
                print(f"Erro: Estoque insuficiente. Saldo atual: {estoque[nome_produto]['quantidade']}")
        else:
            print(f"Erro: O produto '{nome_produto}' não foi encontrado.")

    elif opcao == "4":
        print("\nEncerrando o sistema da DataCode Solutions... Até logo!")
        break 

    else:
        # Este é o bloco de 'fallback' para qualquer entrada que não seja 1, 2, 3 ou 4
        print(f"\n[ERRO] A opção '{opcao}' é inválida. Por favor, escolha um número de 1 a 4.")
    