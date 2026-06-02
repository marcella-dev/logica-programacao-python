def validar_autenticacao(limite_tentativas: int = 3) -> bool:
    """
    Simula o sistema de validação de acesso de segurança de uma aplicação.
    Garante o controle de tentativas de login para mitigar acessos indevidos.
    """
    CREDENCIAL_MESTRA = "1234"
    tentativas_restantes = limite_tentativas

    print("<><><><><><> VALIDAÇÃO DE ACESSO <><><><><><>")

    while tentativas_restantes > 0:
        credencial_input = input(f"Digite a senha de acesso ({tentativas_restantes} tentativas restantes): ").strip()
        
        if credencial_input == CREDENCIAL_MESTRA:
            print("\n\033[0;32m[SUCESSO]\033[m Autenticação confirmada. Acesso concedido ao sistema.")
            return True
        else:
            tentativas_restantes -= 1
            print("\033[0;31m[ERRO]\033[m Credencial incorreta!")

    print("\n\033[0;31m[BLOQUEIO]\033[m Limite de tentativas excedido. Acesso negado.")
    return False

# Bloco de execução principal do script
if __name__ == "__main__":
    validar_autenticacao()