ano = int(input('Ano do nascimento: '))

idade = 2026 - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14: 
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
elif idade > 25:
    print('Classificação: MASTER')