num = int(input('Me diga um numero qualquer: '))

resultado = num % 2

if resultado == 0:
    print('O numero {} e par'.format(num))
else:
    print('O numero {} e impar'.format(num))