from utilidades import strings, numeros
try:
    strings.tema('Média do semestre')
    nota_1 = float(input('Qual a primeira nota:'))
    nota_2 = float(input('Qual a segunda nota:'))
    strings.pul()
    strings.div()
    print(numeros.media(nota_1,nota_2))
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