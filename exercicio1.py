palavra_secreta = "python"
max_erros = 6

while True:  # LOOP DO JOGO

    tentativas = 0
    erros = 0
    letras_adivinhadas = ""

    print("=" * 50)
    print("BEM-VINDO AO JOGO DE PALAVRA SECRETA!")
    print("=" * 50)
    print(f"A palavra tem {len(palavra_secreta)} letras")
    print(f"Você pode errar até {max_erros} vezes\n")

    while True:  # LOOP DA PARTIDA

        # Mostrar palavra
        display = ""
        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                display += letra + " "
            else:
                display += "* "

        print(f"\nPalavra: {display}")
        print(f"Tentativas: {tentativas} | Erros: {erros}/{max_erros}")

        # Entrada do usuário
        while True:
            letra = input("Digite uma letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Digite apenas UMA letra válida!")
                continue

            if letra in letras_adivinhadas:
                print("⚠️ Você já tentou essa letra!")
                continue

            break

        tentativas += 1

        # Processar letra
        if letra in palavra_secreta:
            letras_adivinhadas += letra
            print(f"✅ A letra '{letra}' está na palavra!")
        else:
            erros += 1
            print(f"❌ A letra '{letra}' NÃO está na palavra!")

        # ✅ VERIFICAÇÃO CORRETA DE VITÓRIA
        if all(l in letras_adivinhadas for l in palavra_secreta):
            print(f"\n🎉 VOCÊ VENCEU! A palavra era '{palavra_secreta}'")
            print(f"📊 Total de tentativas: {tentativas}")
            break

        # Derrota
        if erros >= max_erros:
            print(f"\n💀 GAME OVER! A palavra era '{palavra_secreta}'")
            print(f"📊 Total de tentativas: {tentativas}")
            break

    # Jogar novamente
    while True:
        resposta = input("\nDeseja jogar novamente? (S/N): ").lower()
        if resposta == "s":
            break
        elif resposta == "n":
            print("Obrigado por jogar! Até logo 👋")
            exit()
        else:
            print("Digite apenas S ou N!")
