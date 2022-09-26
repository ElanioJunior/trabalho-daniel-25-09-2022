num1 = int(input('digite um numero: '))
num2 = int(input('digite um numero: '))
num3 = int(input('digite um numero: '))

if num1 > num3 > num2:
    print('a sequencia é {}>{}>{}'.format(num1, num3, num2))

elif num1 > num2 > num3:
    print('a sequencia é {}>{}>{}'.format(num1, num2, num3))

elif num2 > num1 > num3:
    print('a sequencia é {}>{}>{}'.format(num2, num1, num3))

elif num2 > num3 > num1:
    print('a sequencia é {}>{}>{}'.format(num2, num3, num1))

elif num3 > num2 > num1:
    print('a sequencia é {}>{}>{}'.format(num3, num2, num1))

elif num3 > num1 > num2:
    print('a sequencia é {}>{}>{}'.format(num3, num1, num2))
