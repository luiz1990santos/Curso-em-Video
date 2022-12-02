from utilidades import strings, numeros

try:
    a = (float(input('Digite o ângulo desejado:')))
    strings.pul()
    numeros.angulo(a)
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





