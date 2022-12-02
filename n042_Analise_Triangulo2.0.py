from utilidades import strings, numeros

try:
    strings.tema('Analisador de triângulos 2.0')
    r1 = float(input('Primeiro seguimento: '))
    r2 = float(input('Segundo seguimento: '))
    r3 = float(input('Terceiro seguimento: '))
    strings.div()
    numeros.triangulo2(r1, r2, r3)
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
