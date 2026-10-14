import re

cpf_enviado_usuario = re.sub('[^0-9]', '', '74682489070')

nove_digitos = cpf_enviado_usuario[:9]
contagem_regressiva_1 = 10
resultado_digito_1 = 0


for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contagem_regressiva_1
    contagem_regressiva_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0 


dez_digitos = nove_digitos + str(digito_1)
contagem_regressiva_2 = 11 

resultado_digito_2 = 0

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contagem_regressiva_2
    contagem_regressiva_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_gerado == cpf_enviado_usuario:
    print(f"CPF válido: {cpf_gerado}")
else:
    print("CPF inválido")