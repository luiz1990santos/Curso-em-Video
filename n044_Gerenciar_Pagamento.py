from utilidades import strings, numeros

try:
    strings.tema('GERENCIADOR DE PAGAMENTOS')
    strings.pul()
    strings.div3()
    numeros.gerenciarPag()
    strings.div3()
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