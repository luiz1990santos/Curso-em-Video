from utilidades import strings, numeros
try:
    strings.tema('TABUADA')
    numero = int(input('Digite um número para ver sua tabuada:'))
    strings.pul()
    strings.div2()
    numeros.tabuada(numero)
    strings.div2()
except ValueError:
    strings.pul()
    strings.div()
    print('Deve digitar um valor numérico.')
    strings.div()
except KeyboardInterrupt:
    strings.pul()
    strings.div()
    print('Programa encerrado!')
    strings.div()