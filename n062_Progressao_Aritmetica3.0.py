from utilidades import strings, numeros

try:
    strings.tema('Gerador de PA 3.0')
    primeiro = int(input('Qual o primeiro termo: '))
    razao = int(input('Qual da PA: '))
    strings.pul()
    strings.div4()
    numeros.progressao_aritm3(primeiro, razao)
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
