from utilidades import strings, numeros

try:
    strings.tema('Analisador de triângulos')
    r1 = float(input('Primeiro seguimento: '))
    r2 = float(input('Segundo seguimento: '))
    r3 = float(input('Terceiro seguimento: '))
    strings.pul()
    strings.div4()
    numeros.triangulo(r1, r2, r3)
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