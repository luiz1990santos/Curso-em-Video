from utilidades import strings, numeros

try:
    strings.tema('Calculo do IMC')
    p = float(input('Digite seu peso(Kg): '))
    a = float(input('Agora digite sua altura(m): '))
    strings.pul()
    strings.div4()
    numeros.imc(p, a)
    strings.div4()
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
