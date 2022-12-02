from utilidades import strings, numeros

try:
    num = int(input('Digite um número: '))
    strings.pul()
    numeros.primo(num)
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