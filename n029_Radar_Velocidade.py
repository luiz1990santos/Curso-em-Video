from utilidades import strings, numeros

try:
    strings.tema('Radar de velocidade')
    v = float(input('Qual a velocidade atual de um carro:'))
    strings.pul()
    strings.div()
    numeros.radar(v)
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

