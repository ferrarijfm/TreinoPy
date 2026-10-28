distancia = float(input('Qual a distancia da sua viagem? '))

print(distancia)
if distancia < 200:
    valor = distancia * 0.50 
    print('Voce esta prestes a comecar uma viagem de {:.1f}Km.'.format(distancia))
    print('E o preco da sua passagem sera de R${:.2f}'.format(valor))
else:
    valor2 = distancia * 0.45
    print('Voce esta prestes a comecar uma viagem de {:.1f}Km.'.format(distancia))
    print('E o preco da sua passagem sera de R${:.2f}'.format(valor2))