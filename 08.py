print('Menu de opções:\n1. somar dois números\n2. raiz quadrada de um número\n')
n1 = int(input('digite a opção desejada'))
if n1 == 1:
    n1 = int(input('digite um numero'))
    n2 = int(input('digite um numero'))
    n3 = n1 + n2
    print('a soma dos dois numeros é:{}'.format(n3))

elif n1 == 2:
    n1 = int(input('digite um numero:'))
    n2 = n1 ** (1/2)
    print('a raiz quadrada de {} é {}'.format(n1, n2))



