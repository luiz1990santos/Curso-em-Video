from utilidades import strings

try:
    f = str(input('Escreva uma frase:').upper().strip())
    strings.pul()
    strings.div()
    strings.verifFrase(f)
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
