from utilidades import strings, numeros

try:
    c = float(input('Qual a temperatura:'))
    strings.pul()
    strings.div4()
    numeros.convTemp(c)
    strings.div4()
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
