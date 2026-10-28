from random import randrange
from time import sleep
num = randrange(0,5)
print("-=-"*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print("-=-"*20)

resp = int((input("Em que número eu pensei? ")))

print("PROCESSANDO...")
sleep(2)


if resp == num:
    print('PARABENS! Você conseguiu me vencer.')
else:
    print(f'GANHEI! Eu pensei no número {num} e não no {resp}!')