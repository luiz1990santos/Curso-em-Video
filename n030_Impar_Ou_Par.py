from utilidades import strings, numeros

try:
    strings.tema('Impar ou Par')
    n = int(input('Digite um número: '))
    strings.pul()
    strings.div4()
    numeros.imparPar(n)
    strings.div4()
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

