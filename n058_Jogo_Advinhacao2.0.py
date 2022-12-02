from utilidades import strings, numeros

try:
    strings.tema('Adivinhe o número que estou pensando')
    strings.pul()
    numeros.jogoaAv2()
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

