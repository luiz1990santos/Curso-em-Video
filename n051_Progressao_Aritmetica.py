from utilidades import strings, numeros

try:
    strings.tema('PROGRESSÃO ARITMÉTICA')
    p = int(input('Qual o primeiro elemento: '))
    r = int(input('Qual a razão: '))
    strings.pul()
    strings.div()
    numeros.progAritm(p, r)
    strings.div()
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
