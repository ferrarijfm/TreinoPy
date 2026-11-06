from random import randint
from time import sleep
jokenpo = ['pedra','papel','tesoura']
j1 = int(input('Suas opções:\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\nQual é a sua jogada? ')) - 1 
j2 = randint(0,2)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 20)
print(f'Computador jogou {jokenpo[j2]}')
print(f'Jogadoror jogou {jokenpo[j1]}')
print('-=' * 20)
if j2 == 0: #pedra
    if j1 == 0:
        print('EMPATE') 
    elif j1 == 1:
        print('JOGADOR VENCE')
    elif j1 == 2:
        print('COMPUTADOR VENCE')
    
elif j2 == 1: #papel
    if j1 == 0:
        print('COMPUTADOR VENCE') 
    elif j1 == 1:
        print('EMPATE')
    elif j1 == 2:
        print('JOGADOR VENCE')
       
elif j2 == 2: #tesoura
    if j1 == 0:
        print('JOGADOR VENCE') 
    elif j1 == 1:
        print('COMPUTADOR VENCE')
    elif j1 == 2:
        print('EMPATE')
       


