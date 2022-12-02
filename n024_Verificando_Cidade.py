from utilidades import strings

try:
    c = input('Qual a sua cidade: '.strip().title())
    strings.pul()
    strings.div()
    strings.verifCidade(c)
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