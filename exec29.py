km = int(input('Qual e a velocidade atual do carro? '))

if km >  80:
    multa = 7 * (km - 80)
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    print(f'Voce deve pagar uma multa de R${multa:.2f}')
else:
    print('Tenha um bom dia! Dirija com seguranca!')