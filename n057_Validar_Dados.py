from utilidades import strings

try:
    strings.tema('QUAL O SEXO')
    sexo = str(input('Qual o seu sexo: ')).strip().upper()[0]
    strings.div()
    strings.validador_dados(sexo)
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
