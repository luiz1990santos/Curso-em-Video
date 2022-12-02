from utilidades import strings, numeros

try:
    strings.tema('SEQUÊNCIA DE FIBONACCI')
    strings.pul()
    strings.div3()
    numero = int(input('Quantos termos você quer mostrar: '))
    strings.div3()
    numeros.fibonacci(numero)
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
