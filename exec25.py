silva = 'silva'

nome = str(input("Qual o seu nome completo: ")).strip()


validador = silva in nome.lower()

print(f'Seu nome tem silva? {validador}')