from utilidades import strings, numeros

try:
    n = str(input('Nome do jogador: '))
    g = str(input('Número de gols: '))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    if n.strip() == '':
        strings.ficha(gols=g)
    else:
        strings.ficha(n, g)
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