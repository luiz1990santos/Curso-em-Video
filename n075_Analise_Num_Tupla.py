from utilidades import strings, numeros

try:
    strings.tema('ANALISE DE DADOS EM UMA TUPLA')
    numero = (int(input('Digite um número: ')),
              int(input('Digite outro número: ')),
              int(input('Digite mais um número: ')),
              int(input('Digite o último número: ')))
    numeros.analise_numeros(numero)
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
