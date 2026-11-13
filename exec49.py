n = int(input('Digite um numero para ver sua tabuada: '))

print('=' * 15)
for num in range(1, 11):
    res = n * num
    print('{} x  {} = {}'.format(n, num, res))
print('=' * 15)