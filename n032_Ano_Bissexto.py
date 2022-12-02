from utilidades import strings
try:
    a = int(input('Que ano você quer analisar? Coloque 0 caso queira o ano atual:'))
    strings.pul()
    strings.div()
    strings.anoBi(a)
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