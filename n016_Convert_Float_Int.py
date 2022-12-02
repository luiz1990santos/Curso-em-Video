from utilidades import numeros, strings

try:
    n = float(input('Digite um número real:'))
    strings.pul()
    strings.div3()
    numeros.floatToInt(n)
    strings.div3()
except ValueError:
    strings.pul()
    strings.div()
    print('Deve digitar um valor numérico.')
    strings.div()
except KeyboardInterrupt:
    strings.pul()
    strings.div()
    print('Programa encerrado!')
    strings.div()
finally:
    print('FIM')
