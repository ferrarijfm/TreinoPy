'''santo = 'santo'
cidade = str(input('Em qual cidade você nasceu? ')).strip()

tratamento = cidade.lower()
validar = santo in tratamento

print(validar)'''


cid = str(input("Em qual cidade você nasceu? ")).strip()

print(cid[:5].lower() == "santo")