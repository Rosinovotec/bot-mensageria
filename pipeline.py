import random

# --- Nosso "Canal" de Alertas ---
def enviar_alerta(status, texto):
    print()

    if status == "sucesso":
        print("=== ALERTA DE SUCESSO ===")
        print("Mensagem:", texto)
        print("=========================")
    else:
        print("=== ALERTA DE ERRO ===")
        print("Mensagem:", texto)
        print("======================")

    print()


# --- Função que Simula o Build ---
def executar_build():
    # Sorteia 1 (sucesso) ou 2 (falha)
    resultado = random.randint(1, 2)

    if resultado == 1:
        return True
    else:
        return False


# --- Programa Principal ---
build_sucesso = executar_build()

if build_sucesso:
    enviar_alerta(
        "sucesso",
        "O build da versão 1.2.0 foi concluído."
    )
else:
    enviar_alerta(
        "erro",
        "O build falhou no commit 'a3b1c9'."
    )
