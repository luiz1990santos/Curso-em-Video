from utilidades import strings, numeros

try:
    o = float(input('Qual o comprimento do cateto oposto:'))
    a = float(input('Qual o comprimento do cateto adjacente:'))
    strings.pul()
    numeros.hiptenusa(o, a)
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
