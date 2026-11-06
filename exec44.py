preco = float(input("Preço das compras: R$"))
opc = int(input('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\nQual é a opção? '))

if opc == 1: 
    desc = preco - (preco * 0.10)
    print(f'Com o desconto de 10%, o valor da compra é R${desc:.2f}')
elif opc == 2:
    desc = preco - (preco * 0.05)
    print(f'Com o desconto de 5%, o valor da compra é R${desc:.2f}')
elif opc == 3:
    print(f'O preço continua o mesmo sem desconto aplicado')
elif opc == 4:
    parc = int(input('Quantas parcelas? '))
    juros = preco * 0.20
    parcelamento = (preco + juros) / parc
    print(f'Sua compra será parcelada em {parc}x de R${parcelamento:.2f} com juros\nSua compra de R${preco:.2f} vai custar R${preco + juros:.2f} no final')