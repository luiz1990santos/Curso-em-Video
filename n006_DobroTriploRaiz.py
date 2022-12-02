from utilidades import strings, numeros
try:
    strings.tema('DOBRO, TRIPLO E RAIZ')
    numero = int(input('Digite um número:'))
    strings.pul()
    strings.div()
    print(numeros.dobro(numero))
    print(numeros.triplo(numero))
    print(numeros.raiz(numero))
    strings.div()
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