pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))

maior = []
menor = []
#Verifica qual e maior 
if pri > seg and pri > ter:
    maior.append(pri)
elif seg > pri and seg > ter:
    maior.append(seg)
elif ter > pri and ter > seg: 
    maior.append(ter)

#Verifica qual e menor
if pri < seg and pri < ter:
    menor.append(pri)
elif seg < pri and seg < ter:
    menor.append(seg)
elif ter < pri and ter < seg: 
    menor.append(ter)

print(f'O menor valor digitado foi {menor[0]}')
print(f'O maior valor digitado foi {maior[0]}')