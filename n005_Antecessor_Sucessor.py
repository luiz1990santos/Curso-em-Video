from utilidades import strings, numeros
try:
    strings.tema('Qual o antecessor e sucessor???')
    numero = int(input('Qual o número:'))
    strings.pul()
    strings.div()
    print(numeros.ant_suc(numero))
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
