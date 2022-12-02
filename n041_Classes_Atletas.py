from utilidades import strings, numeros

try:
    strings.tema('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
    nome = str(input('\nAtleta qual o seu nome: '))
    nasc = int(input(f'\nOla {nome} qual seu ano de nascimento: '))
    strings.pul()
    strings.div()
    numeros.atleta(nome, nasc)
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


