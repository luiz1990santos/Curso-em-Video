from utilidades import strings, numeros

try:
    strings.tema('VAMOS JOGAR PAR OU IMPAR?')
    strings.div2()
    numeros.jogo_par_impar()
    strings.div2()
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
