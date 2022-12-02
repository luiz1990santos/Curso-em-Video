from utilidades import strings, numeros
try:
    while True:
        strings.tema('CALCULADORA')
        opcao = int(input('''
        O que deseja fazer?
        [1] SOMAR
        [2] SUBTRAIR
        [3] DIVIDIR
        [4] MULTIPLICAR
        [5] SAIR
        =>  '''))
        if opcao == 5:
            strings.div()
            print('Você encerrou.')
            break
        elif 0 >= opcao or opcao > 5:
            strings.div4()
            print('Opção escolhida não é válida.')
            strings.div4()
        else:
            n1 = int(input('Digite o primeiro número:'))
            n2 = int(input('Digite o segundo número:'))
            strings.pul()
            strings.div5()
            print(numeros.calculadora(n1, n2, opcao))
            strings.div5()
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
    print('Volte sempre!')
    strings.div()
