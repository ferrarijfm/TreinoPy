altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

area = largura * altura
litros = area * 0.50
# a cada 2m quadrados voce usa 1 L de tinta
print('Sua parede tem a dimensao de {}x{} e sua area e de {:.2f}ms quadrados .\nPara pintar essa parede, voce precisara de {:.2f}l de tinta .'.format(largura, altura, area, litros))

