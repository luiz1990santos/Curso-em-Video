from utilidades import strings, numeros
try:
    t = int(input('Digite qual tabuada deseja: '))
    strings.div()
    numeros.tab2(t)
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

