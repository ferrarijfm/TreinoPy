print("=" * 20)
print(" 10 TERMOS DE UMA PA ")
print("=" * 20)

pt = int(input("Primeiro termo: "))
rz = int(input("Razão: "))

for n in range(pt,pt + 9 * rz + rz, rz ):
    print(n, end=' ->')
print("ACABOU")