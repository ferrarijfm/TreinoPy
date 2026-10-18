#Primeira solução
"""import random
alunos = []

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

alunos.append(aluno1)
alunos.append(aluno2)
alunos.append(aluno3)
alunos.append(aluno4)

alunoEscolhido = random.randrange(0, 3)


print("O aluno escolhido foi {}".format(alunos[alunoEscolhido]))
"""

#Melhor solução 
from random import choice

a1 = str(input("Primeiro aluno: "))
a2 = str(input("Segundo aluno: "))
a3 = str(input("Terceiro aluno: "))
a4 = str(input("Quarto aluno: "))

alunos = [a1, a2, a3, a4]

print(f"O aluno escolhido foi {choice(alunos)}")