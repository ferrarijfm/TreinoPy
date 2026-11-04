casa = float(input('Valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))

parcela = casa / (anos * 12) 
minimo = salario * 0.30

if parcela <= minimo:
    print(f"Para pagar um casa de R${casa:.2f} em {anos} anos a prestação será de R${parcela:.2f} \nEmpréstimo deve ser CONCEDIDO!")
elif parcela > minimo:
    print(f"Para pagar um casa de R${casa:.2f} em {anos} anos a prestação será de R${parcela:.2f} \nEmpréstimo deve ser NEGADO!")









