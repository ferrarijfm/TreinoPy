'''numero = str(input('Informe um numero: '))

separador = numero.strip()

print('Unidade: {}'.format(numero[-1]))
print('Dezena: {}'.format(numero[-2]))
print('Centena: {}'.format(numero[-3]))
print('Milhar: {}'.format(numero[-6:-3]))

'''


numero = int(input('Informe um número: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')