from utilidades import strings, numeros

try:
    strings.tema('NÚMERO POR EXTENSO')
    strings.div2()
    numeros.numero_extenso()
    strings.div2()
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
