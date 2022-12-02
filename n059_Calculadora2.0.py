from utilidades import strings, numeros

try:
    strings.tema('CALCULADORA 2.0')
    strings.pul()
    strings.div()
    numeros.calculadora2()
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
