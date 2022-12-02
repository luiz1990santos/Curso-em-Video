from utilidades import strings, numeros

try:
    strings.tema('Portal de alistamento')
    n = int(input('Digite o ano de nascimento para consulta: '))
    strings.div()
    numeros.alistamento(n)
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




