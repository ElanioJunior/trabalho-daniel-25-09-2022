nota1 = float(input('digite uma nota'))
nota2 = float(input('digite uma nota'))
nota3 = float(input('digite uma nota'))

#Processamento de dados
media = float(nota1 + nota2 + nota3) /3

if 3 >= media >= 0:
    print('a sua média de {} te deixa reprovado'.format(media))

elif 5 >= media >= 4:
    print('a sua média de {} te deixa em recuperação'.format(media))

elif 10 >= media >= 6:
    print('a sua média de {} te deia aprovado'.format(media))

else:
    print('a sua nota precisa ser entre 1 e 10')
