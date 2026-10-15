preco = float(input('Qual o preco do produto: R$'))

desconto  = preco - (preco * 0.05)

print('O produto que custava {}, na promocao com desconto de 5% vai custa R${:.2f}'.format(preco, desconto))