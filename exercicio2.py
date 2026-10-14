ListaDeCompras = []

while True:
    print("selecione uma opção")
    opcao = input("[i]nserir, [a]pagar, [l]istar: ")


    if opcao == "i":
        item = input("O que deseja inserir? ")
        ListaDeCompras.append(item)
        print(f"{item} foi adicionado à lista.")


    elif opcao == "a":
        indice_str = input("Escolha qual item quer apagar (ex: 1, 0 ou 6) : ")
        indice = int(indice_str)
        del ListaDeCompras[indice]
        print(f"{item} foi removido da lista.")


    elif opcao == "l":
        if len(ListaDeCompras) == 0 : 
            print("A lista de compras está vazia.")
            continue
        print("Itens na lista de compras:")
        for i, item in enumerate(ListaDeCompras):
            print(i, item)


    else:
        print("Opção inválida. Tente novamente")