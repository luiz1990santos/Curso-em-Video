from utilidades import strings, numeros

try:
    strings.div2()
    p = int(input('Primeiro:'))
    s = int(input('Segundo:'))
    t = int(input('Terceiro:'))
    strings.div2()
    strings.pul()
    strings.div()
    numeros.maiorMenor(p, s, t)
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