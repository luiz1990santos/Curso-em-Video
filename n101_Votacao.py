from utilidades import strings, numeros

try:
    ano = int(input('Digite o ano de nascimento: '))
    strings.div()
    print(strings.voto(ano))
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

