from utilidades import strings, numeros
try:
    strings.tema('CONVERSOR DE MEDIDA')
    distancia = float(input('Uma distância em metros:'))
    strings.pul()
    strings.div()
    print(numeros.conversor_medida(distancia))
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
