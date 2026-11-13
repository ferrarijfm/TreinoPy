soma = 0
contador = 0
for n in range(1,7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f"A soma de todos {contador} os  valores solicitados é {soma}")
