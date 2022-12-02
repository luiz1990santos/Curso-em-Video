from utilidades import strings, numeros

try:
    strings.tema('Comparação de pesos')
    strings.div()
    numeros.compararPeso()
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



