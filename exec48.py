soma = 0
contador = 0
for n in range(1,501,2):
    if n % 3 == 0:
        soma += n
        contador += 1
print(f"A soma de todos {contador} os  valores solicitados é {soma}")

