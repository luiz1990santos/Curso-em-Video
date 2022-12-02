from utilidades import strings, numeros
try:
    strings.tema('Conversor de bases numéricas')
    o = int(input('''1 para Binário
    2 para Octal
    3 para Hexadecimal 
    Escolha qual a Base de conversão: '''))
    n = int(input('\nDigite o número que deseja converter: '))
    strings.pul()
    strings.div4()
    numeros.convBase(o, n)
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

