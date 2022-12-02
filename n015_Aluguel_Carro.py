from utilidades import strings, numeros

try:
    strings.tema('ALUGUEL DE CARRO')
    while True:
        strings.div2()
        opcao = str(input('''
        MENU:
            [S] Consulta 
            [N] Sair
        => ''').upper()[0])
        strings.div2()
        if opcao in 'Ss':
            d = int(input('Quantos dias ficou com o carro:'))
            k = int(input('Quantos Km foram rodados: '))
            strings.pul()
            strings.div()
            numeros.alugCar(d, k)
        elif opcao in 'Nn':
            break
        else:
            print('Opcão errada!')
    strings.div()
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
finally:
    strings.pul()
    strings.div()
    print('FIM')
    strings.div()
