from utilidades import strings

try:
    n = str(input('Digite o seu nome completo:'.strip()))
    strings.pul()
    strings.verifStrings(n)
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

