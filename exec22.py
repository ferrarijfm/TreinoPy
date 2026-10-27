nome = input(str('Digite seu nome completo: '))
maiuscula = nome.upper()
minusculas = nome.lower()
tamanho = len(nome) - nome.count(' ')
separador = nome.split()
primeironome = separador[0]


print('Analisando seu nome...')
print(f'Seu nome em maiusculas e {maiuscula}')
print(f'Seu nome me minusculas e {minusculas}')
print(f'seu nome tem ao todo {tamanho}')
print(f'Seu primeiro nome e {primeironome} e ele tem {len(primeironome)} letras')

