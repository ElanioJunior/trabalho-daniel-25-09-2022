dia = int(input('digite um dia'))
mes = int(input('digite um mês'))
ano = int(input('digite um ano'))

print('agora digite outra data')

dia2 = int(input('digite um dia'))
mes2 = int(input('digite um mês'))
ano2 = int(input('digite um ano'))

if ano > ano2:
    print('a data {}/{}/{} é maior que {}/{}/{}'.format(dia, mes, ano))

if ano2 > ano:
    print('a data {}/{}/{} é maior que {}/{}/{}'.format(dia2, mes2, ano2))