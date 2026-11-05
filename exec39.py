ano = int(input('Ano de nascimento: '))

alistamento = 2026 - ano 

if alistamento == 18:
    print(f'Quem nasceu em {ano} tem {alistamento} anos em 2026.\nVocê deve se alistar imediatamente!')
elif alistamento < 18:
    temp = 18 - alistamento    
    print(f"Quem nasceu em {ano} tem {alistamento} anos em 2026.\nAinda faltam {temp} anos para o alistamento\nSeu alistamento será em {2026 + temp}")
elif alistamento > 18: 
    temp = alistamento - 18
    print(f"Quem nasceu em {ano} tem {alistamento} anos em 2026.\nVocê já deveria ter se alistado há {temp} anos.\nSeu alistamento foi em {2026 - temp}")
    