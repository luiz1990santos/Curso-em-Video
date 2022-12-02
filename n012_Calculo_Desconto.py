from utilidades import strings, numeros
try:
    strings.tema('Promoção 5% OFF')
    valor = int(input('Qual o valor do produto:'))
    strings.pul()
    strings.div()
    print(f'Valor do produto R${valor:,.2f}, com desconto de 5% é R${numeros.desconto(valor):,.2f}')
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