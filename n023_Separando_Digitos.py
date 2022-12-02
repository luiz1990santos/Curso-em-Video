from utilidades import numeros, strings

try:
    numero = input('Digite um número entre 0000 e 9999: ')
    strings.pul()
    strings.div()
    numeros.verifNum(numero)
    strings.div()
except IndexError:
    print(' ERRO! Nenhum número foi digitado.')
    strings.div()
except KeyboardInterrupt:
    strings.pul()
    strings.div()
    print('Programa encerrado!')
    strings.div()
finally:
    strings.pul()
    print('FIM')
