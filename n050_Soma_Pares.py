from utilidades import strings, numeros

try:
    strings.tema('SOMA DE NÚMEROS PARES')
    strings.div5()
    numeros.somaPares()
    strings.div5()
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


