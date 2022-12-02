from utilidades import numeros

while True:
    inteiro = int()
    real = float()
    try:
        inteiro = int(input('Digite um número inteiro: '))
        real = float(input('Digite um número real: '))
    except ValueError:
        print('Digite um valor correto.')
    except KeyboardInterrupt:
        print('\nUsuário preferiu não digitar um numero o valores.')
        print(f'O numero inteiro foi {numeros.leia_int2(inteiro)}')
        print(f'O numero real foi {numeros.leia_float(real)}')
        break
    else:
        print(f'O numero inteiro foi {numeros.leia_int2(inteiro)}')
        print(f'O numero real foi {numeros.leia_float(real)}')
        break
