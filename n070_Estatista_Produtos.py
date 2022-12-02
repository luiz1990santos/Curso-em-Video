from utilidades import strings

try:
    strings.tema('LOJA SUPER PRICE')
    strings.div2()
    strings.produtos()
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