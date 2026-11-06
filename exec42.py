a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))


if a + b > c and a + c > b and b + c > a and a == b == c:
    print("Os segmentos acima PODEM FORMAR EQUILÁTERO!")
elif a + b > c and a + c > b and b + c > a and a == b or b == c or c == a:
    print("Os segmentos acima PODEM FORMAR ISÓSCELES!")
elif a + b > c and a + c > b and b + c > a and a != b != c :
    print("Os segmentos acima PODEM FORMAR ESCALENO!")
else:
    print("Os segmentos acima NAO PODEM FORMAR triangulo!")