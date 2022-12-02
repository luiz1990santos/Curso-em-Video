from utilidades import strings, numeros

try:
    strings.tema('Comparador de números')
    p = int(input('Primeiro número: '))
    s = int(input('Segundo número: '))
    strings.pul()
    strings.div()
    numeros.comparar(p, s)
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

