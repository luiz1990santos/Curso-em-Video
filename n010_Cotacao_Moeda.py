from utilidades import numeros, strings

try:
    strings.tema('COMPRAR DOLARES')
    while True:
        escolha = int(input('O que deseja fazer? [1] para NOVA CONSULTA ou [0] para SAIR ]: '))
        if escolha == 0:
            break
        elif escolha == 1:
            strings.pul()
            strings.div()
            numeros.dolar_atual()
            strings.div()
            real = float(input('Qual o Valor em reais: '))
            strings.pul()
            strings.div()
            print(numeros.cotacao(real))
            strings.div()
        else:
            print('Opcão inválida.')
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
    strings.div()
    print('Volte sempre.')
    strings.div()
    