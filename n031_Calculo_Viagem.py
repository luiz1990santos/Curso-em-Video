from utilidades import strings, numeros
try:
    strings.tema('Calculo de viagem')
    d = float(input('Qual a distância da sua viagem(km): '))
    strings.pul()
    strings.div()
    numeros.calcViagem(d)
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

