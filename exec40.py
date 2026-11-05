nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media =  (nota1 + nota2) / 2

if media >= 7.0:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}\nO aluno está Aprovado')
elif media < 5.0:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}\nO aluno está Reprovado')
else:
    print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}\nO aluno está Recuperação')