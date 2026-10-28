from datetime import date

ano = int(input("Que ano quer analisar? Coloque zero para analisar o ano atual: "))


if ano == 0:
    ano = date.today().year
    bissexto = ano % 4 == 0 and ano % 100 != 0 and ano % 400
    if bissexto == 0:
        print(f'O ano {ano} e BISSEXtO')
elif ano % 4 == 0 and ano % 100 != 0 and ano % 400 :
    print(f'O ano {ano} e BISSEXTO')
else:
    print(f'O ano {ano} nao e BISSEXTO')