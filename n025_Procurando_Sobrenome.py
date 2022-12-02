from utilidades import strings

try:
    n = input('Qual o seu nome: ')
    strings.pul()
    strings.div()
    strings.verifNome(n)
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