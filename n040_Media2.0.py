from utilidades import strings,numeros

try:
    strings.tema('Faculdade L Santos')
    n1 = float(input('Qual a primeira nota: '))
    n2 = float(input('Qual a segunda nota: '))
    strings.pul()
    strings.div()
    numeros.media2(n1, n2)
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