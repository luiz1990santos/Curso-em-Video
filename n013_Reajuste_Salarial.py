from utilidades import strings, numeros
try:
    strings.tema('Aumento de salário')
    salario = float(input('Qual o salário do funcionário:'))
    strings.pul()
    strings.div()
    print(f'Seu salário era R${salario:,.2f}, com os 15% ficou R${numeros.reajuste(salario):,.2f}')
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