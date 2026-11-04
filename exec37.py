

num = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão")
print("[ 1 ]converter para BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL")
opc = int(input("Sua opção: "))

if opc == 1:
    resultado = bin(num)
    print(f"{num} convertido para BINÁRIO é igual a {resultado[2:]}")
elif opc == 2:
    resultado = oct(num)
    print(f"{num} convertido para OCTAL é igual a {resultado[2:]}")
elif opc == 3:
    resultado = hex(num)
    print(f"{num} convertido para HEXADECIMAL é igual a {resultado[2:]}")