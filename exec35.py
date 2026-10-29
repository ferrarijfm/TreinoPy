print('-=-' * 20)
print('Analisador de Triangulos')
print('-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print("Os segmentos acima PODEM FORMAR triangulo!")
else:
    print("Os segmentos acima NAO PODEM FORMAR triangulo!")