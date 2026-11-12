soma = 0
contador = 0
for n in range(1,501,2):
    if n % 3 == 0:
        contador = contador + 1
        soma = soma + n
print(f"A soma de todos {contador} os  valores solicitados é {soma}")

