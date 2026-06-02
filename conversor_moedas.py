import requests


def buscar_cotacoes_tempo_real() -> dict:
    """
    Camada de Ingestão: Consome a API pública AwesomeAPI para capturar
    as cotações atualizadas de mercado em tempo real (USD e EUR em relação ao BRL).
    Retorna um dicionário com as cotações ou valores padrão em caso de falha.
    """
    URL_API = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    
    # Cotações de contingência (caso a internet falhe, o sistema não quebra)
    COTACOES_BACKUP = {"USD": 4.93, "EUR": 5.76}
    
    try:
        # Realiza a requisição HTTP GET na API
        resposta = requests.get(URL_API, timeout=5)
        
        # Se a requisição foi bem-sucedida (Status Code 200)
        if resposta.status_code == 200:
            dados_api = resposta.json()  # Faz o parsing do JSON recebido
            
            # Extrai e converte as cotações reais atualizadas
            cotacao_dolar = float(dados_api["USDBRL"]["bid"])
            cotacao_euro = float(dados_api["EURBRL"]["bid"])
            
            return {"USD": cotacao_dolar, "EUR": cotacao_euro, "fonte": "API Tempo Real"}
            
    except (requests.RequestException, KeyError, ValueError):
        # Tratamento de erro de rede ou parsing de dados
        pass
        
    return {"USD": COTACOES_BACKUP["USD"], "EUR": COTACOES_BACKUP["EUR"], "fonte": "Backup Local"}


def executar_conversor_cambial():
    """
    Camada de Processamento e Interface: Gerencia a interação, 
    chama o extrator de dados cambiais e executa a conversão.
    """
    print("=" * 50)
    print(f"{'PIPELINE DE NORMALIZAÇÃO CAMBIAL':^50}")
    print("=" * 50)

    try:
        entrada_real = input('Digite o valor em moeda nacional (R$): ').strip().replace(",", ".")
        valor_real = float(entrada_real)

        if valor_real <= 0:
            print("[ALERTA] O valor para conversão deve ser estritamente maior que zero.")
            return

    except ValueError:
        print("[ERRO CRÍTICO] Entrada monetária inválida. Digite apenas números.")
        return

    # Ingestão de dados externos via API
    print("\nConectando ao provedor de dados financeiros...")
    dados_cambio = buscar_cotacoes_tempo_real()
    
    print(f"Cotações obtidas via: {dados_cambio['fonte']}\n")
    print("Escolha a moeda de destino para conversão:")
    print(f"1 - Dólar Comercial (Cotação atual: $ {dados_cambio['USD']:.2f})")
    print(f"2 - Euro Comercial  (Cotação atual: € {dados_cambio['EUR']:.2f})")
    
    moeda_escolhida = input('\nSua opção (1 ou 2): ').strip()

    # Processamento das regras de conversão
    if moeda_escolhida == '1':
        total_convertido = valor_real / dados_cambio['USD']
        print("\n" + "═" * 50)
        print(f" Com R$ {valor_real:.2f} você pode adquirir US$ {total_convertido:.2f}")
        print("═" * 50)
        
    elif moeda_escolhida == '2':
        total_convertido = valor_real / dados_cambio['EUR']
        print("\n" + "═" * 50)
        print(f" Com R$ {valor_real:.2f} você pode adquirir € {total_convertido:.2f}")
        print("═" * 50)
        
    else:
        print('[ERRO OPERACIONAL] Opção de conversão de câmbio inválida.')


if __name__ == "__main__":
    executar_conversor_cambial()