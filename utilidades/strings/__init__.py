def ola():
    return f'Ola mundo!'


def tema(msg):
    tam = len(msg) + 2
    print('==' * tam)
    print(msg)
    print('==' * tam)


def usuario(n='Desconhecido', i='0'):
    print(f'O usuário(a) {n.strip().title()} tem {i} anos.')


def nasc(d, m, a):
    from datetime import date
    ano_atual = date.today()
    i = int(ano_atual.year) - a
    mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
           7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    print('Sua data de nascimento é ', end='')
    if m == 1:
        print(f'{d} de {mes[1]} de {a}', end='')
    elif m == 2:
        print(f'{d} de {mes[2]} de {a}', end='')
    elif m == 3:
        print(f'{d} de {mes[3]} de {a}', end='')
    elif m == 4:
        print(f'{d} de {mes[4]} de {a}', end='')
    elif m == 5:
        print(f'{d} de {mes[5]} de {a}', end='')
    elif m == 6:
        print(f'{d} de {mes[6]} de {a}', end='')
    elif m == 7:
        print(f'{d} de {mes[7]} de {a}', end='')
    elif m == 8:
        print(f'{d} de {mes[8]} de {a}', end='')
    elif m == 9:
        print(f'{d} de {mes[9]} de {a}', end='')
    elif m == 10:
        print(f'{d} de {mes[10]} de {a}', end='')
    elif m == 11:
        print(f'{d} de {mes[11]} de {a}', end='')
    elif m == 12:
        print(f'{d} de {mes[12]} de {a}', end='')
    print(f', tem {i} ano(s)')


def pul():
    print('\n')


def div():
    print('--' * 53)


def div2():
    print('**' * 53)


def div3():
    print('-_' * 53)


def div4():
    print('-=' * 53)


def div5():
    print('++' * 53)


def sorte(aluno1, aluno2, aluno3, aluno4):
    import random
    lista = [aluno1, aluno2, aluno3, aluno4]
    sorteio = random.choice(lista)
    print(f'O aluno escolhido foi {sorteio.title()}')


def ordem(aluno1, aluno2, aluno3, aluno4):
    import random
    lista = [aluno1.title(), aluno2.title(), aluno3.title(), aluno4.title()]
    random.shuffle(lista)
    print(f'A ordem de apresentação será ', end='')
    print(f'{lista[0]}, {lista[1]}, {lista[2]} e {lista[3]}')


def music():
    import pygame
    pygame.init()
    pygame.mixer.music.load('n021_TocadorMp3.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()


def verifStrings(nome):
    from time import sleep
    print('Analisando as informações...')
    sleep(1)
    print(f'Seu nome em maiúsculas: {nome.upper()}')
    sleep(1)
    print(f'Seu nome em minúsculas: {nome.lower()}')
    sleep(1)
    letras = nome.replace(' ', '')
    print(f'Seu nome tem ao todo {len(letras)} letras.')
    sleep(1)
    primeiro = nome.split()
    print(f'Seu primeiro nome é {primeiro[0]} e tem {len(primeiro[0])} letras')
    sleep(1)


def verifCidade(cidade):
    if 'santo' in cidade:
        print(f'O nome da cidade {cidade} começa com Santo!')
    else:
        print(f'O nome da cidade {cidade} não começa com Santo!')


def verifNome(nome):
    if 'Silva' in nome:
        print(f'{nome} seu nome tem Silva.')
    else:
        print(f'{nome} seu nome não tem Silva.')


def verifFrase(frase):
    """
    :param frase:
    :return:
    """
    print(f'A letra A aparece {frase.count("A")} vezes')
    print(f'A primeira letras aparece na posição {frase.find("A") + 1}')
    print(f'A última letra A aparece no posição {frase.rfind("A") + 1}')


def manipularNome():
    nome, sobrenome = list(map(str, input('Digite o seu nome completo: ').split()))
    print(f'Primeiro: {nome}')
    print(f'Último: {sobrenome}')


def anoBi(ano):
    from datetime import date
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é BISSEXTO')
    else:
        print(f'O ano {ano} não é BISSEXTO')


def jukenpo(jogador, computador):
    from time import sleep
    print('\nJO')
    sleep(0.6)
    print('KEN')
    sleep(0.6)
    print('PÔ\n')

    if jogador == 0 and computador == 2:
        print('''
        GANHOU!
        ''')
    elif jogador == 2 and computador == 1:
        print('''
        GANHOU!! 
        ''')
    elif jogador == 1 and computador == 0:
        print('''
        GANHOU! 
        ''')
    if jogador == 2 and computador == 0:
        print('''
        PERDEU! 
        ''')
    elif jogador == 1 and computador == 2:
        print('''
        PERDEU!
        ''')
    elif jogador == 0 and computador == 1:
        print('''
        PERDEU!
        ''')
    elif jogador == 0 and computador == 0 or jogador == 1 and computador == 1 or jogador == 2 and computador == 2:
        print('EMPATE!')


def palin(frase):
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    print(f'Você digitou a frase {junto} e o inverso dela é {inverso}.')
    if inverso == junto:
        print('Temos um palindromo.')
    else:
        print('Não temos um palindromo.')


def AnaliseGrupos():
    from datetime import date
    totalmaior = 0
    totalmenor = 0
    for numero in range(1, 8):
        ano_atual = date.today().year
        nascimento = int(input(f'{numero} - Qual o ano de nascimento: '))
        idade = ano_atual - nascimento
        if idade >= 21:
            totalmaior += 1
        else:
            totalmenor += 1

    print(f'''\n{totalmaior} pessoas são maiores de idade.
    {totalmenor} pessoas são menores de idade ainda.\n''')


def analise_dados():
    print('*' * 100)
    print(' ' * 37, 'ANALISADOR DE DADOS')
    print('*' * 100)
    contador = 0
    soma = 0
    maiorIdadeH = 0
    nomeVelho = ''
    totalMulher = 0
    for pessoas in range(1, 5):
        print('\n')
        print(f'{pessoas}ª PESSOA')
        nome = str(input('NOME: ')).strip()
        idade = int(input('IDADE: '))
        sexo = str(input('SEXO (M/F): ')).strip()
        soma += idade / 4
        if pessoas == 1 and sexo in 'Mm':
            maiorIdadeH = idade
            nomeVelho = nome
        if sexo in 'Mm' and idade > maiorIdadeH:
            maiorIdadeH = idade
            nomeVelho = nome
        if sexo in 'Ff' and idade < 20:
            totalMulher += 1
        soma += idade / 4
    print(f'A média de idade do grupo é de {soma} anos.')
    print(f'O homem mais velho tem {maiorIdadeH} anos e se chama {nomeVelho}')
    print(f'Ao todo são {totalMulher} mulheres com menos de 20 anos')


def validador_dados(sexo):
    while sexo not in 'MmFf':
        sexo = str(input(f'\n{sexo} não é um sexo válido, tente novamente:')).strip().upper()[0]
    print(f'Sexo {sexo} registrado com sucesso.')


def analise_grupos2():
    opcao = ''
    contador = 0
    homem = 0
    idadeMaior = 0
    menorMulher = 0
    while opcao != 'Nn':
        print('-' * 40)
        print(' ' * 8, 'CADASTRE UMA PESSOA')
        print('-' * 40)
        idade = int(input('Idade: '))
        sexo = str(input('Sexo: (M/F) ')).upper().strip()[0]
        print('-' * 40)
        opcao = str(input('Quer continuar: (S/N) ')).upper().strip()[0]

        if idade >= 18:
            idadeMaior += 1
        if sexo in 'Mm':
            homem += 1
        if sexo in 'Ff' and idade < 20:
            menorMulher += 1
        if opcao in 'Nn':
            print(f'Total de pessoas com mais de 18 anos: {idadeMaior}')
            print(f'Ao todo temos {homem} homen(s) cadastrados')
            print(f'E temos {menorMulher} mulhere(s) com menos de 20 anos')
            break


def produtos():
    opcao = ''
    total = 0
    maiorPreco = 0
    barato = ''
    menorPreco = 0
    contador = 0
    while opcao != 'Nn':
        produto = str(input('Nome do produto: ')).upper().lower().strip()
        preco = float(input('Preço: R$'))
        opcao = str(input('Quer continuar? (S/N) ')).upper().strip()[0]
        total = total + preco
        contador += 1
        if preco > 1000:
            maiorPreco += 1
        if contador == 1:
            menorPreco = preco
            barato = produto
        else:
            if preco < menorPreco:
                menorPreco = preco
                barato = produto
        if opcao in 'Nn':
            print('------------ FIM DO PROGRAMA ------------')
            print(f'O total da compra foi R${total:.2f}')
            print(f'Temos {maiorPreco} produto(s) custando mais de R$1000.00 ')
            print(f'O produto mais barato foi {barato} que custa R${menorPreco:.2f}')
            break


def times():
    import emoji
    print(emoji.emojize(':soccer_ball:') * 21)
    print('CAMPEONATO BRASILEIRO DE FUTEBOL')
    print(emoji.emojize(':soccer_ball:') * 21)

    campeonato = ('Palmeiras', 'Corinthians', 'Athletico PR', 'Atlético-MG', 'Internacional',
                  'Fluminense', 'Botafogo', 'Santos', 'São Paulo', 'Red Bull Bragantino', 'Avaí',
                  'Atlético-GO', 'Ceará', 'Flamengo', 'Coritiba', 'América-MG', 'Goiás', 'Cuiabá-MT',
                  'Fortaleza', 'Juventude')
    print('\n')
    print(emoji.emojize(':soccer_ball:') * 194)
    print(f'Lista de times: {campeonato}')
    print(emoji.emojize(':soccer_ball:') * 194)
    print(f'As 5 primeiras colocações do campeonato são:\n{campeonato[0:5]}')
    print(emoji.emojize(':soccer_ball:') * 194)
    print(f'As 4 últimas posições são: \n{campeonato[15:20]}')
    print(emoji.emojize(':soccer_ball:') * 194)
    print(sorted(campeonato))
    print(emoji.emojize(':soccer_ball:') * 194)
    print(f' O time {campeonato[8]} está na posição ', end='')
    print(campeonato.index('São Paulo'))
    print(emoji.emojize(':soccer_ball:') * 194)


def precos():
    lista = (('Creatina', 42.3),
             ('Whey Protein', 144.0),
             ('BCAA', 50.4),
             ('Multivitamínico', 35.0),
             ('Cafeína', 54.0),
             ('Termogênico', 67.5),
             ('L-Glutamina', 45.0),
             ('L-Carnitina', 72.0),
             ('Dextrose', 18.0))
    print('-' * 40)
    print(' ' * 10, 'LISTAGEM DE PREÇOS')
    print('-' * 40)
    for n in lista:
        print(f'{n[0]:.<30} R${n[1]:7.2f}')
    print('-' * 40)


def contador_vogais():
    palavras = ('aprender', 'programar', 'linguagem', 'python',
                'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
                'mercado', 'programador', 'futuro')
    for c in palavras:
        print(f'\nNa palavra {c.upper()} temos ', end='')
        for letras in c:
            if letras.lower() in 'aeiou':
                print(f'{letras.upper()} ', end='')


def validador_expressao(exp):
    pilha = []
    for simbulo in exp:
        if simbulo == '(':
            pilha.append('(')
        elif simbulo == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        print('Sua expressão está correta.')
    else:
        print('Sua expressão está errada.')


def analisar_lista():
    pessoas = []
    dados = []
    maiorPeso = 0
    menorPeso = 0
    contador = 0
    while True:
        dados.append(str(input('Digite o nome: ')))
        dados.append(int(input('Qual o peso(Kg): ')))
        if len(pessoas) == 0:
            maiorPeso = menorPeso = dados[1]
        else:
            if dados[1] > maiorPeso:
                maiorPeso = dados[1]
            if dados[1] < menorPeso:
                menorPeso = dados[1]
        pessoas.append(dados[:])
        dados.clear()
        escolha = str(input('Quer continuar: '))
        contador += 1
        if escolha in 'Nn':
            break
    print('=' * 80)
    print(f'Ao todo, foram cadastradas {contador} pessoas.')
    print('-' * 80)
    for peso in pessoas:
        if peso[1] == maiorPeso:
            print(f'O maior peso foi {maiorPeso} de {peso[0]}')
        if peso[1] == menorPeso:
            print(f'O menor peso foi {menorPeso} de {peso[0]}')


def analisar_medias():
    ficha = list()
    while True:
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        ficha.append([nome, nota1, nota2, media])
        resposta = str(input('QUER CONTINUAR(S/N): '))
        if resposta in 'Nn':
            break
    print('=' * 30)
    print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
    print('-' * 30)
    for indice, aluno in enumerate(ficha):
        print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
        print('-' * 30)
    while True:
        print('-' * 35)
        opcao = int(input('Mostrar nota de qual aluno? (999 para SAIR)'))
        if opcao == 999:
            print('FINALIZANDO...')
            break
        if opcao <= len(ficha) - 1:
            print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
        print('volte sempre')


def media_dicionario():
    aluno = dict()
    aluno['Nome'] = str(input('Nome do aluno: '))
    aluno['Media'] = float(input('Qual a média: '))
    if aluno['Media'] <= 6:
        aluno['Situação'] = 'Reprovado'
    else:
        aluno['Situação'] = 'Aprovado'
    print('=' * 35)
    for chave, valor in aluno.items():
        print(f'{chave} é igual {valor}')
    print('=' * 35)


def jogar_dados():
    from random import randint
    from time import sleep
    from operator import itemgetter

    jogo = {'Jogador 1': randint(1, 6),
            'Jogador 2': randint(1, 6),
            'Jogador 3': randint(1, 6),
            'Jogador 4': randint(1, 6)}
    ranking = list()
    print('=' * 30)
    for chave, valor in jogo.items():
        sleep(1)
        print(f'{chave} tirou o número {valor}')
    print('=' * 30)
    ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
    for indice, valor in enumerate(ranking):
        sleep(1)
        print(f'{indice + 1}º Lugar foi {valor[0]} ele tirou {valor[1]}')
    print('=' * 30)


def cadastrar_funcionario():
    from datetime import datetime
    print('=' * 40)
    print(' ' * 8, 'CALCULO TRABALHADOR')
    print('=' * 40)
    trabalhador = dict()
    print('-' * 55)
    trabalhador['nome'] = str(input('Nome do trabalhador: '))
    nascimento = int(input('Qual o ano de nascimento: '))
    trabalhador['idade'] = datetime.now().year - nascimento
    trabalhador['ctps'] = int(input('Número da carteira de trabalho: '))
    if trabalhador['ctps'] == 0:
        pass
    else:
        trabalhador['contrato'] = int(input('Ano de contratação: '))
        trabalhador['salario'] = float(input('Digite o salário: '))
        trabalhador['aposentadoria'] = (trabalhador['idade'] + trabalhador['contrato'] + 35) - datetime.now().year

    print('-' * 55)
    print('\n')
    print('RESULTADO:')
    print('-' * 55)
    print(f'Nome: {trabalhador["nome"]}')
    print(f'Idade: {trabalhador["idade"]}')
    if trabalhador['ctps'] == 0:
        print('Não possui Carteira de trabalho.')
    else:
        print(f'Número da Carteira de trabalho: {trabalhador["ctps"]}')
        print(f'Contratado em: {trabalhador["contrato"]}')
        print(f'Salário: R${trabalhador["salario"]:.2f}')
        print(f'Idade da aposentadoria: {trabalhador["aposentadoria"]}')
    print('-' * 55)


def cadastro_jogador():
    from time import sleep

    def separador():
        print('-=' * 48)

    jogador = dict()
    partidas = list()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
    for c in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['gols'] = partidas[:]  # Para colocar a lista dentro do dicionario
    jogador['total'] = sum(jogador['gols'])  # cria a soma.
    separador()
    print(jogador)
    separador()
    for chave, valor in jogador.items():
        sleep(0.5)
        print(f'O campo {chave} tem o valor {valor}.')
    separador()
    print(f'O jogador {jogador["nome"]} jogou {total} partidas.')
    for chave, valor in enumerate(jogador['gols']):
        sleep(0.5)
        print(f'    => Na partida {chave}, fez {valor} gol(s).')
    print(f'Foi um total de {jogador["total"]} gol(s).')


def analise_dados2():
    def decor():
        print('=' * 45)

    def pular():
        print('\n')

    decor()
    print(' ' * 7, 'ANÁLISE DE DADOS COMPLETO')
    decor()
    pular()
    pessoas = list()
    dados = dict()
    decor()
    contador = 0
    soma = 0
    media = 0
    while True:
        dados.clear()
        dados['nome'] = str(input('Nome: '))
        dados['sexo'] = str(input('Sexo(M/F): ')).upper()[0]  # pega só a primeira letra
        if dados['sexo'] not in 'MmFf':
            while True:
                if dados['sexo'] in 'MmFf':
                    break
                else:
                    print('ERRO! Responda apenas M ou F.')
                    dados['sexo'] = str(input('Sexo(M/F): ').upper())
        dados['idade'] = int(input('Idade: '))
        soma += dados['idade']
        pessoas.append(dados.copy())
        opcao = str(input('Quer continuar(S/N): ')).upper()[0]
        contador += 1
        if opcao in 'Ss':
            continue
        elif opcao in 'Nn':
            break
        while True:
            if opcao not in 'nNsS':
                print('Erro! Responda apenas S ou N.')
                opcao = str(input('Quer continuar(S/N): ')).upper()
            else:
                break
    decor()
    print(f'Ao todo temos {contador} pessoas cadastradas.')
    media = soma / len(pessoas)
    print(f'A média de idade é de {media:5.2f}')
    print(f'As mulheres cadastrados foram ', end='')
    for p in pessoas:
        if p['sexo'] in 'Ff':
            print(f'{p["nome"]} ', end='')
    print()
    print('Lista das pessoas que estão acima da média: ')
    for p in pessoas:
        if p['idade'] >= media:
            print('  ')
            for k, v in p.items():
                print(f'{k} = {v}; ', end='')
            print()
    decor()
    print('>> ENCERRADO <<')


def cadastro_jogador2():
    from time import sleep

    def sep():
        print('-=' * 48)

    time = list()
    jogador = dict()
    partidas = list()

    while True:
        jogador.clear()
        jogador['nome'] = str(input('Nome do jogador: '))
        total = int(input(f'Quantos partidas {jogador["nome"]} jogou? '))
        partidas.clear()
        for c in range(0, total):
            partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
        jogador['gols'] = partidas[:]  # Para colocar a lista dentro do dicionario
        jogador['total'] = sum(jogador['gols'])  # cria a soma.
        time.append(jogador.copy())
        opcao = str(input('Quer continuar(S/N): ')).upper()[0]
        if opcao in 'Ss':
            continue
        elif opcao in 'Nn':
            break
        while True:
            if opcao not in 'nNsS':
                print('Erro! Responda apenas S ou N.')
                opcao = str(input('Quer continuar(S/N): ')).upper()[0]
            else:
                break
    sep()
    print('cod', end='')
    for i in jogador.keys():
        print(f'{i:<15}', end='')
    print()
    sep()
    for k, v in enumerate(time):
        sleep(0.5)
        print(f'{k:>3} ', end='')
        for d in v.values():
            print(f'{str(d):<15} ', end='')
        print()
    sep()
    while True:
        busca = int(input('Mostrar os dados de qual jogador:(Parar 999) '))
        if busca == 999:
            break
        elif busca >= len(time):
            print(f'Erro! Não existe o jogador de codigo {busca}')
        else:
            print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
            sleep(1)
            for i, q in enumerate(time[busca]['gols']):
                print(f'  No jogo {i} fez {q} gols.')
            sep()
    print('>>> VOLTE SEMPRE <<<')


def escreva(msg):
    tamanho = len(msg)+3
    print('~'*tamanho)
    print(f' {msg}')
    print('~'*tamanho)


def voto(ano):
    from datetime import date #Escopo
    from time import sleep
    atual = date.today().year
    idade = atual - ano
    print('Aguarde...')
    sleep(1)
    if idade < 16:
        return f'{idade} anos, não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade} anos, voto opcional.'
    else:
        return f'{idade} anos, voto obrigatório.'


def ficha(jog='Desconhecido',gols=0):
    print(f'O jogador {jog} fez {gols} gol(s) na temporada.')


def ajuda(funcao):
    import time
    import datetime
    import pandas
    import random
    import pygame
    import math
    import tkinter
    import django
    import numpy
    import emoji
    import email
    import kivy
    import flask
    import requests
    print(f'Acessando o manual do comando {funcao}', 2)
    time.sleep(1)
    print('AGUARDE...', 6)
    time.sleep(1.5)
    help(funcao)


def leia_opcao(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            ok = True
        else:
            print('ERRO! Digite um número inteiro vãlido.')
        if ok:
            break
    return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1
    print(linha())
    opc = leia_opcao('Sua Opção: ')
    return opc


def cadastro_pessoas(nome, idade):
    pessoas = {'nome': 'idade'}
    pessoas = open('../../pessoas.txt', 'w')
    pessoas.write(f'{pessoas["nome"]}\n\n\n{pessoas["idade"]} ano(s)')
    pessoas.close()


def pessoas_cadastradas():
    pessoas = open('../../pessoas.txt', 'r')
    for k, v in pessoas.keys():
        print(f'{k}\t\t{v}')
    pessoas.close()
