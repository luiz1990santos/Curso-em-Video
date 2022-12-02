from utilidades import strings, numeros

try:
    strings.tema('Banco Python Financiamentos S.A.')
    i = float(input('Qual o valor do imóvel a ser financiado(R$): '))
    r = float(input('Qual a sua renda mensal(R$): '))
    p = int(input('Em quantos parcelas(até 420 meses): '))
    strings.pul()
    strings.div()
    numeros.emprestimo(i, r, p)
    strings.div()
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


