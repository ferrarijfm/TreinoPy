from math import radians, sin, cos, tan

valor = float(input("Digite o angulo que voce deseja: "))

seno = sin(radians(valor))
cosseno = cos(radians(valor))
tangente = tan(radians(valor))

print(f"O angulo de {valor} tem o SENO de {seno:.2f}")
print(f"O angulo de {valor} tem o COSSENO de {cosseno:.2f}")
print(f"O angulo de {valor} tem a TANGENTE de {tangente:.2f}")