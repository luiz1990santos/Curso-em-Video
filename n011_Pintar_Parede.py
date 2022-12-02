from utilidades import strings, numeros
try:
    largura = float(input('Qual a largura da parede:'))
    altura = float(input('Qual a altura da parede:'))
    strings.pul()
    strings.div()
    numeros.pintar(largura, altura)
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