from utilidades import strings, numeros

try:
    strings.tema('=== Fatorial ===')
    strings.pul()
    numero = int(input('Digite um número: '))
    strings.div()
    numeros.fatorial(numero)
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
