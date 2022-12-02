from utilidades import strings, numeros

try:
    strings.tema('AUMENTO SALARIAL')
    s = float(input('Qual é o sálario do funcionário: R$'))
    strings.pul()
    strings.div2()
    numeros.sal(s)
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
