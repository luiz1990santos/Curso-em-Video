from utilidades import strings

try:
    funcao = ''
    while True:
        strings.tema('SISTEMA DE DOCUMENTAÇÃO PYTHON')
        funcao = str(input('Função ou Biblioteca >>> ').strip())
        if funcao.upper() == 'SAIR':
            break
        else:
            strings.ajuda(funcao)
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
