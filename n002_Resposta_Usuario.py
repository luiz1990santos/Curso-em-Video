from utilidades import strings
try:
    while True:
        strings.tema('Dados do Usuário')
        nome = str(input('Digite o seu nome: '))
        sua_idade = str(input('Qual a sua idade: '))
        strings.pul()
        if sua_idade.isnumeric():
            idade = int(sua_idade)
        else:
            idade = 0
        if nome == '':
            strings.div3()
            strings.usuario()
            strings.div3()
        else:
            strings.div3()
            strings.usuario(nome, sua_idade)
            strings.div3()
except KeyboardInterrupt:
    strings.pul()
    strings.div()
    print('Programa encerrado!')
    strings.div()
