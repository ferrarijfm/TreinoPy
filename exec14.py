opcao = str(input("Este é um conversor de temperatura \nDigite F para fahrenheit e C para celsius:"))

if opcao == "C" or opcao == "c":
    celsius = float(input("Informe a temperatura em °C: "))
    fahrenheit = (celsius * 9 / 5) + 32 
    print("A temperatura de {:.1f}°C corresponde a {:.1f}°F".format(celsius, fahrenheit))
elif opcao == "F" or opcao == "f":
    fahrenheit = float(input("Informe a temperatura em °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("A temperatura de {:.1f}°f corresponde a {:.1f}°C".format(fahrenheit, celsius))
else:
    print("Digite uma opção valida!")