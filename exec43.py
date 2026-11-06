peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a usa altura? (m) '))

imc = peso / (altura * altura)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Morbida') 