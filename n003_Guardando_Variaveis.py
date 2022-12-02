from utilidades import strings
from time import sleep

strings.tema('Data de Nascimento')
idade = int()
try:
    while True:
        sleep(0.5)
        dia = int(input('Digite o dia de nascimento:'))
        if dia < 1 or dia > 31:
            strings.div4()
            print(f'O {dia} não é um dia válido, deve ser entre 1 e 31.')
            strings.div4()
        else:
            break
    while True:
        sleep(0.5)
        mes = int(input('Digite o mês de nascimento:'))
        if mes < 1 or mes > 12:
            strings.div4()
            print(f'O {mes} não é um mês válido, deve ser entre 1 e 12')
            strings.div4()
        else:
            break
    while True:
        sleep(0.5)
        ano = int(input('Digite o ano de nascimento:'))
        if ano < 1900 or ano > 2022:
            strings.div4()
            print(f'O {ano} não é um ano válido, ', end='')
            if ano < 1900:
                print('está muito a baixo do esperado.')
                strings.div4()
            elif ano > 2022:
                print('o limite é o ano atual.')
                strings.div4()
        else:
            break
    strings.pul()
    strings.div4()
    strings.nasc(dia, mes, ano)
    strings.div4()
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
