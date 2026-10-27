frase = str(input("Digite uma frase: ")).strip().lower()

contador = frase.count('a')
primeira = frase.find('a')
#ultima = frase.find('a', -1,)
ultima = frase.rfind('a')

print("A letra A apareceu {} vezes na frase.".format(contador))
print("A primeira letra A apareceu na posição {}.".format(primeira + 1))
print("A última letra A apareceu na posição {}.".format(ultima))
