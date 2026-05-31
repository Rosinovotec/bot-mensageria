# Função para enviar alertas
def enviar_alerta(status, servico, autor, commit_hash):
    print()

    if status == "sucesso":
        print("✅ SUCESSO: Deploy concluído!")
        print("-----------------------------------")
        print("Serviço:", servico)
        print("Autor(a):", autor)
        print("Commit:", commit_hash)
        print(f"Link: https://github.com/empresa/{servico}/commit/{commit_hash}")
        print("-----------------------------------")
    else:
        print("⚠️ ATENÇÃO: O build falhou.")
        print("-----------------------------------")
        print("Serviço:", servico)
        print("Autor(a) do último commit:", autor)
        print("Commit da falha:", commit_hash)
        print("Ação recomendada: Verificar os logs do build.")
        print("Link para os logs: https://ci.empresa.com/builds/123/logs")
        print("-----------------------------------")

    print()


# Programa principal
resultado = int(input("Digite 1 para sucesso ou 2 para falha: "))

if resultado == 1:
    enviar_alerta(
        "sucesso",
        "servico-de-pagamentos",
        "Maria Silva",
        "7a3b1f9"
    )
elif resultado == 2:
    enviar_alerta(
        "erro",
        "servico-de-login",
        "João Souza",
        "a4c2d8e"
    )
else:
    print("Opção inválida! Digite apenas 1 ou 2.")
