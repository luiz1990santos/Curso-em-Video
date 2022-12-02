import random
from utilidades import strings

try:
    strings.tema('JOGO JUKENPÔ')
    print('''Vamos Jogar? 
    0 - PEDRA 
    1 - PAPEL
    2 - TESOURA
    ''')
    itens = ('PEDRA', 'PAPEL', 'TESOURA')
    computador = random.randint(0, 2)
    jogador = int(input('Qual você escolhe: '))
    strings.jukenpo(jogador, computador)
    print(f'Computador jogou {itens[computador]}')
    print(f'Você jogou {itens[jogador]}')
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