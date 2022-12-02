from utilidades import strings, numeros

try:
    strings.tema(' Soma dos Números digitados ')
    strings.div()
    numeros.tratamento_numeros()
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

