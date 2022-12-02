from utilidades import strings, numeros

try:
    while True:
        a1: str = input('Primeiro aluno: ')
        a2: str = input('Segundo aluno: ')
        a3: str = input('Terceiro aluno: ')
        a4: str = input('Quarto aluno: ')
        strings.pul()
        strings.div3()
        strings.sorte(a1, a2, a3, a4)
        strings.div3()
        opcao = int(input('Quer continuar? [1]SIM ou [2]NÃO: '))
        if opcao == 1:
            continue
        elif opcao == 2:
            break
        else:
            print('Opção inválida.')
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
    strings.div4()
    print('FIM')
    strings.div4()

