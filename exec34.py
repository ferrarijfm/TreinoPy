salario = float(input('Qual e o salario do funcionario? R$'))

if salario <= 1250:
    reajuste = salario + (salario * 0.15)
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${reajuste:.2f} agora.')
else:
    reajuste = salario + (salario * 0.10) 
    print(f'Quem ganhava R${salario:.2f} passa a ganhar R${reajuste:.2f} agora.')