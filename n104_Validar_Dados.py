from utilidades import strings, numeros

try:
    n = numeros.leiaInt('Digite um número: ')
    strings.div4()
    print(f'Você acabou de digitar o número {n}.')
    strings.div4()
except ValueError:
    strings.pul()
    strings.div()
    print('Valor inválido.')
    strings.div()
except KeyboardInterrupt:
    strings.pul()
    strings.div()
    print('Programa encerrado!')
    strings.div()
finally:
    strings.pul()
    print('FIM')