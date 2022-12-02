def calculadora(a, b, c):
    if c == 1:
        return f'\t\t\t\t\t\t{a} + {b} = {a + b}'
    elif c == 2:
        return f'\t\t\t\t\t\t{a} - {b} = {a - b}'
    elif c == 3:
        return f'\t\t\t\t\t\t{a} / {b} = {a / b}'
    elif c == 4:
        return f'\t\t\t\t\t\t{a} * {b} = {a * b}'


def ant_suc(n):
    a = n - 1
    s = n + 1
    return f'Número {n}, o antecessor dele é {a} e o sucessor é {s}.'


def dobro(n):
    d = n * 2
    return f'O dobro de {n} vale {d}'


def triplo(n):
    t = n * 3
    return f'O triplo de {n} vale {t}'


def raiz(n):
    r = n ** (1 / 2)
    return f'A raiz de {n} é igual a {r:.2f}'


def media(n1, n2):
    m = float(n1 + n2) / 2
    return f'Suas notas foram {n1} e {n2} sua média foi {m}'


def conversor_medida(m):
    cm = float(m * 100)
    mm = float(m * 1000)
    return f'A medida de {m:.1f} metros corresponde a {cm:.1f} centímetros e {mm:.1f} milímetros.'


def tabuada(n):
    print(f'{n} X {1} = {n * 1}')
    print(f'{n} X {2} = {n * 2}')
    print(f'{n} X {3} = {n * 3}')
    print(f'{n} X {4} = {n * 4}')
    print(f'{n} X {5} = {n * 5}')
    print(f'{n} X {6} = {n * 6}')
    print(f'{n} X {7} = {n * 7}')
    print(f'{n} X {8} = {n * 8}')
    print(f'{n} X {9} = {n * 9}')
    print(f'{n} X {10} = {n * 10}')


def dolar_atual():
    import requests
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        d = response.json()['USD']['low']
        print(f'O dolar pela cotação atual é US${float(d):,.2f}')


def cotacao(r):
    import requests
    url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
    response = requests.get(url)
    if response.status_code == 200:
        d = response.json()['USD']['low']
        v = r / float(d)
        return f'Com R${r:,.2f}, você consegue comprar US${v:,.2f}'


def pintar(l, a):
    area = l * a
    t = a / 2
    print(f'Sua parede tem a dimensão de {l:.1f}X{a:.1f} e a sua área é de {area:,.1f}m².')
    print(f'Para pintar essa parede, você vai precisar de {t:,.1f}l de tinta.')


def desconto(v):
    d = v - (v * 5 / 100)
    return d


def reajuste(s):
    a = s + (s * 15 / 100)
    return a


def convTemp(celsius):
    fahrenheit = 32 + (celsius * 1.8)
    print(f'Temperatura {celsius}ºC convertida é {fahrenheit}ºF. ')


def alugCar(dias, km):
    valorDias = dias * 60
    valorKm = km * 0.15
    total = valorDias + valorKm
    print(f'Valor do aluguel é de R${valorDias:,.2f}')
    print(f'O custo de km é R${valorKm:,.2f}')
    print(f'O Total de despesas é R${total:,.2f}')


def floatToInt(numero):
    print(f'O valor digitado foi {numero} e sua porção inteira é {int(numero)}')


def hiptenusa(oposto, adjacente):
    hip = (oposto ** 2 + adjacente ** 2) ** (1 / 2)
    print(f'A hipotenusa vai medir {hip:,.2f}')


def angulo(ang):
    import math
    seno = math.sin(math.radians(ang))
    cosseno = math.cos(math.radians(ang))
    tangente = math.tan(math.radians(ang))
    print(f'O ãngulo de {ang}º tem o SENO de {seno:.2f}')
    print(f'O ãngulo de {ang}º tem o COSSENO de {cosseno:.2f}')
    print(f'O ãngulo de {ang}º tem a TANGENTE de {tangente:.2f}')


def verifNum(numero):
    from time import sleep
    print(f'Analisando o número {numero} ele tem', end=' ')
    sleep(2)
    print(f'Unidade: {numero[3]},', end=' ')
    sleep(1)
    print(f'Dezena: {numero[2]},', end=' ')
    sleep(1)
    print(f'Centena: {numero[1]},', end=' ')
    sleep(1)
    print(f'e Milhar: {numero[0]}')


def jogoAdv():
    import random
    from time import sleep
    tentativas = 1
    while tentativas <= 3:
        j = int(input('Qual número estou pensando? Entre 0 e 5 => '))
        c = random.randint(0, 5)
        print('Processando...')
        sleep(1)
        if j > 5:
            print('Erro! Você deve digitar um número entre 0 e 5.')
        else:
            if j == c:
                print(f'O seu foi {j} e o meu {c}, PARABÉNS PENSAMOS NO MESMO NùMERO.')
                break
            else:
                print(f'O seu foi {j} e o meu {c}, VOCÊ ERROU KKKKKKKKKK.')
        tentativas += 1


def radar(velocidade):
    multa = (velocidade - 80) * 7
    if velocidade > 80:
        print('MULTADO! Você excedeu o limite de velocidade de 80km.')
        print(f'Sua velocidade foi {int(velocidade)}km, Você foi multado em R${multa:,.2f}')
    else:
        print('Tenha um Bom Dia, dirija com segurança!')


def imparPar(numero):
    if numero % 2:
        print(f'O número digitado foi {numero}, ele é IMPAR.')
    else:
        print(f'O número digitado foi {numero}, ele é PAR.')


def calcViagem(distancia):
    if distancia <= 0:
        print(f'Não foi possivel calcular a distânia tem que ser maior que {distancia:,.1f}')
    else:
        print(f'Você está prestes a iniciar uma viagem de {distancia:,.1f}km')
        if distancia >= 200:
            preco = distancia * 0.50
        else:
            preco = distancia * 0.45
        print(f'O valor da sua viagem será R${preco:,.2f}')


def maiorMenor(primeiro, segundo, terceiro):
    menor = min(primeiro, segundo, terceiro)
    maior = max(primeiro, segundo, terceiro)
    print(f'O menor valor digitado foi {menor}')
    print(f'O maior valor digitado foi {maior}')


def sal(salario):
    if salario <= 1250:
        percentual = 25
        print(f'- Baseado nos ganhos, o funcionário tem direito a {percentual}%')
    else:
        percentual = 15
        print(f'- Baseado nos ganhos, o funcionário tem direito a {percentual}%')
    nSalario = salario + (salario * percentual / 100)
    valorAumento = nSalario - salario
    print(f'- O sálário de R${salario:,.2f} passou a ser R${nSalario:,.2f}')
    print(f'- Houve um aumento de R${valorAumento:,.2f}')


def triangulo(r1, r2, r3):
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os seguimentos acima podem formar um triângulo.')
    else:
        print('Os seguimentos acima não podem formar um triângulo.')


def emprestimo(imovel, renda, parcelas):
    from time import sleep
    sleep(1)
    print('\nAguarde...\n')
    sleep(2)
    if parcelas > 420:
        print(f'Erro! O limite de parcelas é de 420 vezes35 anos)')
    else:
        print('\n- Dados da proposta -')
        print(f'Valor do Imóvel:R${imovel:,.2f}')
        print(f'Renda mensal:R${renda:,.2f}')
        print(f'Número de parcelas:{parcelas} vezes')
        print('\nOs dados estão corretos? ', end='')
        confirmacao = int(input('Digite 1 para seguir ou 0 para sair: '))
        print('\nProcessando as informações...\n')
        sleep(3)
        if confirmacao == 1:
            taxa = imovel + (imovel * 9.6 / 100)
            parcelamento = taxa / parcelas
            verificacao = (renda * 30 / 100)
            if parcelamento <= verificacao:
                print(f'''\nParabéns seu financiamento foi aprovado!\n 
                Dados:
                Valor do Imóvel financeado: R${imovel:,.2f}
                30% da sua renda: R${verificacao:,.2f}
                Valor das parcelas: R${parcelamento:,.2f}(em {parcelas} vezes)
                Valor total do financiamemto: R${taxa:,.2f}
                 ''')
            else:
                print(f'''\n Infelizmente seu financiamento foi negado!\n
                Renda incompatível com valor de parcelas
                Dados:
                30% da sua renda: R${verificacao:,.2f}
                Valor das parcelas: R${parcelamento:,.2f}''')

        elif confirmacao == 0:
            print('\n Você encerrou, pode voltar a qualquer momento se quiser!')
        else:
            print('\nOPÇÃO INVÁLIDA.\n')


def convBase(opcao, numero):
    if opcao == 1:
        print(f'O número {numero}\033[m convertido em Binário é {bin(numero)[2:]}.')
    elif opcao == 2:
        print(f'O número {numero}\033[m convertido em Octal é {oct(numero)[2:]}.')
    elif opcao == 3:
        print(f'O número {numero}\033[m convertido em Hexadecimal é {hex(numero)[2:]}.')
    else:
        print('Opção inválida.')


def comparar(primeiro, segundo):
    print(f'Você digitou {primeiro} e {segundo}')
    if primeiro > segundo:
        print('O PRIMEIRO número é o MAIOR.')
    elif primeiro < segundo:
        print('O SEGUNDO número é o MAIOR.')
    elif primeiro == segundo:
        print('Os números digitados são IGUAIS.')


def alistamento(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    print(f'\nVocê nasceu no ano de {nascimento} e tem {idade} anos')
    if idade == 18:
        print('Deve se alistar IMEDIATAMENTE')
    elif idade > 18:
        maior = idade - 18
        print(f'Deveria ter se alistado há {maior} anos')
    elif idade < 18:
        menor = 18 - idade
        print(f'Faltam {menor} anos para poder se alistar')


def media2(nota1, nota2):
    from time import sleep
    med = float(nota1 + nota2) / 2
    print('Processando os dados...')
    sleep(2)
    print(f'Suas notas foram {nota1} e {nota2} sua média foi {med}', end='')
    sleep(1)
    if med >= 9:
        print(', você é muito INTELIGENTE.')
    elif med >= 7:
        print(', você foi APROVADO.')
    elif 5 <= med < 6.9:
        print(', você está de RECUPERAÇÃO.')
    elif med < 5:
        print(', você foi REPROVADO.')


def atleta(nome, nascimento):
    from time import sleep
    from datetime import date
    atual = date.today().year
    print('Aguarde...')
    sleep(2)
    idade = atual - nascimento
    print(f'{nome} como você tem {idade} anos', end='')
    sleep(1)
    if idade <= 9:
        print(', sua categoria é MIRIM.')
    elif idade <= 14:
        print(', sua categoria é INFANTIL.')
    elif idade <= 19:
        print(', sua  categoria é JUNIOR.')
    elif idade == 20:
        print(', sua categoria é SÊNIOR.')
    else:
        print(', Sua categoria é MASTER.')


def triangulo2(r1, r2, r3):
    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os seguimentos acima podem formar um triângulo: ', end='')
        if r1 == r2 == r3:
            print('Equilátero')
        elif r1 != r2 != r3 != r1:
            print('Escaleno')
        else:
            print('Isóscele')
    else:
        print('Os seguimentos acima não podem formar um triângulo.')


def imc(peso, altura):
    calculo = peso / (altura * altura)
    print(f'Seu IMC é {calculo:.1f}', end='')
    if calculo <= 18.5:
        print(', você está abaixo do peso.')
    elif calculo <= 25:
        print(', você está no peso ideal.')
    elif calculo <= 30:
        print(', você está no sobrepeso.')
    elif calculo <= 40:
        print(', você está com obesidade.')
    else:
        print(', você está com obesidade mórbida.')


def gerenciarPag():
    while True:
        produto = float(input('\nQual o valor do produto(R$): '))
        pagamento = int(input('''OPÇÕES DE PAGAMENTO:
        1 - À vista(10%Off)
        2 - À vista no cartão(5%Off)
        3 - Em até 2x no cartão
        4 - 3x ou mais no cartão(20% de Juros)
        5 - SAIR
        Qual será a forma de pagamento: '''))
        print(f'\nValor do produto: R${produto:,.2f}')
        if pagamento == 1:
            aVista = produto - (produto * 0.10)
            print(f'\nValor à vista(10%Off) R${aVista:,.2f}')
        elif pagamento == 2:
            aVistaCartao = produto - (produto * 0.05)
            print(f'\nValor à vista no cartão(5%Off) R${aVistaCartao:,.2f}')
        elif pagamento == 3:
            parcelado2x = produto / 2
            print(f'\n2 vezes de R${parcelado2x:,.2f}')
        elif pagamento == 4:
            parcelas = int(input('Deseja parcelar em quantas: '))
            parceladoMais = produto + (produto * 0.20)
            parcelamento = parceladoMais / parcelas
            print(f'\n{parcelas} vezes(com 20% juros) de R${parcelamento:,.2f}(Valor total R${parceladoMais:,.2f})')
        elif pagamento == 5:
            break
        else:
            print('\nOPÇÃO INVÁLIDA.')


def contagem():
    from time import sleep
    for bomb in range(10, -1, -1):
        sleep(1)
        print('\n')
        print(bomb)
    print('\nBOOOMMMMMMMMM')


def contPares():
    for numero in range(2, 51, 2):
        print(numero, end=' - ')
    print('FIM')


def somaImpar():
    soma = 0
    numeros = 0
    for numero in range(1, 501, 2):
        if numero % 3 == 0:
            numeros = numeros + 1
            soma = soma + numero
    print(f'A soma dos {numeros} solicitados é {soma}')


def tab2(tabuada2):
    for numero in range(1, 11):
        resultado = numero * tabuada2
        print(f'  {tabuada2} X {numero} = {resultado}')


def somaPares():
    soma = 0
    contador = 0
    for numero in range(1, 7):
        num = int(input('Digite o {}º: '.format(numero)))
        if num % 2 == 0:
            soma += num
            contador += 1
    print('A soma dos {} número(s) pares digitados é {}.'.format(contador, soma))


def progAritm(primeiro, razao):
    decimo = primeiro + (10 - 1) * razao
    for numero in range(primeiro, decimo + razao, razao):
        print(numero, end=' - ')
    print(' FIM')


def primo(numero):
    total = 0
    for contador in range(1, numero + 1):
        if numero % contador == 0:
            print('\033[33m', end='')
            total += 1
        else:
            print('\033[31m', end='')
        print('{}'.format(contador), end='')
    print(f'\n\033[mO número {numero} foi divisível {total} vezes')
    if total == 2:
        print('E por isso ele é PRIMO.')
    else:
        print('E POR ISSO ELE NÃO É PRIMO.')


def compararPeso():
    maior = 0
    menor = 0
    for pessoas in range(1, 6):
        peso = float(input(f'{pessoas} - Qual o peso da pessoa(Kg): '))
        if pessoas == 1:
            maior = peso
            menor = peso
        else:
            if peso > maior:
                maior = peso
            if peso < menor:
                menor = peso
    print(f'\n{maior:.1f}Kg é o MAIOR PESO.')
    print(f'\n{menor:.1f}Kg é o MENOR PESO.')


def jogoaAv2():
    import random
    from time import sleep
    tentativas = 1
    contador = 0
    while tentativas <= 3:
        computador = random.randint(1, 10)
        jogador = int(input('Digite um número: '))
        tentativas += 1
        contador += 1
        if jogador == computador:
            print(f'\nPensei no {computador}, PARABÉNS VOCÊ ACERTOU!')
            break
        elif jogador < 1 or jogador > 10:
            print('\nO número deve estar entre 0 e 10.\n')
        else:
            if jogador < computador:
                print(f'\nÉ maior que {jogador}!\n')
            else:
                print(f'\nÉ menor que {jogador}!\n')
    print(f'\nVocê tentou {contador} vezes.')
    print('\nFim de jogo!')


def calculadora2():
    opcoes = 0
    while opcoes != 5:
        n1 = int(input('\nDigite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('''\nMENU:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] SABER O MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR 
    ''')
        opcoes = int(input('O que deseja fazer: '))
        if opcoes == 1:
            soma = n1 + n2
            print(f'\n{n1} + {n2} = {soma}')
        elif opcoes == 2:
            multiplicacao = n1 * n2
            print(f'\n{n1} * {n2} = {multiplicacao}')
        elif opcoes == 3:
            print(f'\nEntre {n1} e {n2} ')
            if n1 > n2:
                print('O primeiro número é o MAIOR.')
            elif n1 < n2:
                print('O segundo número é o MAIOR.')
            else:
                print('O números são IGUAIS.')
        elif opcoes == 4:
            n1 = int(input('\nDigite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            print('''\nMENU:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] SABER O MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR 
        ''')
            opcoes = int(input('O que deseja fazer: '))
            if opcoes == 1:
                soma = n1 + n2
                print(f'\n{n1} + {n2} = {soma}')
            elif opcoes == 2:
                multiplicacao = n1 * n2
                print(f'\n{n1} * {n2} = {multiplicacao}')
            elif opcoes == 3:
                print(f'\nEntre {n1} e {n2} ')
                if n1 > n2:
                    print('O primeiro número é o MAIOR.')
                elif n1 < n2:
                    print('O segundo número é o MAIOR.')
                else:
                    print('O números são IGUAIS.')
            elif opcoes == 4:
                n1 = int(input('\nDigite o primeiro número: '))
                n2 = int(input('Digite o segundo número: '))
            elif opcoes == 5:
                print('\nVocê saiu.')
                break
            else:
                print('Opção inválida.')
        elif opcoes == 5:
            print('\nVocê saiu.')
            break
        else:
            print('Opção errada!')


def fatorial(numero):
    contador = numero
    fat = 1
    while contador > 0:
        print(f' {contador} ', end='')
        print('x' if contador > 1 else ' = ', end='')
        fat = fat * contador
        contador -= 1
    print(f'{fat}')


def progressao_aritm2(primeiro, razao):
    termo = primeiro
    contador = 1
    while contador <= 10:
        print(f'{termo} - \n', end='')
        termo += razao
        contador += 1


def progressao_aritm3(primeiro, razao):
    termo = primeiro
    contador = 1
    total = 0
    mais = 10
    while mais != 0:
        total += mais
        while contador <= total:
            print(f'{termo} - \n', end='')
            termo += razao
            contador += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais: '))


def fibonacci(numero):
    termo1 = 0
    termo2 = 1
    print(f'{termo1} - {termo2}', end='')
    contador = 3
    while contador <= numero:
        termo3 = termo1 + termo2
        print(f' - {termo3}', end='')
        termo1 = termo2
        termo2 = termo3
        contador += 1


def tratamento_numeros():
    numero = contador = soma = 0
    while numero != 999:
        soma += numero
        contador += 1
        numero = int(input('Digite um número(999 para parar): '))
    print(f'Você digitou {contador} números e a soma entre eles foi {soma}')


def tratamento_numeros2():
    numero = 0
    contador = 0
    soma = 0
    while True:
        numero = int(input('Digite um número (parar digite 0): '))
        soma += numero
        contador += 1
        if numero == 999:
            break
    print(f'Você digitou {contador} números, a soma deles é {soma - 999}')


def tabuada3():
    tab = 0
    while True:
        tab = int(input('Digite qual tabuada deseja: '))
        print('-' * 30)
        if tab <= 0:
            print('Você saiu.')
            print('-' * 30)
            break
        else:
            for numero in range(1, 11):
                resultado = numero * tab
                print(f'  {tab} X {numero} = {resultado}')
            print('-' * 30)


def jogo_par_impar():
    from random import randint
    from time import sleep
    while True:
        jogador = int(input('Digite um valor: '))
        computador = randint(1, 11)
        soma = jogador + computador
        escolha = ' '
        while escolha not in 'PI':
            escolha = str(input('Par ou Ímpar?(P/I) ')).strip().upper()[0]
        print('--' * 20)
        print(f'Você jogou {jogador} e eu {computador}, total foi {soma}')
        print('--' * 20)
        if escolha in 'Ii':
            sleep(1)
            if soma % 2 == 1:
                print(f'\nVocê GANHOU!\n')
            else:
                print(f'\nDeu PAR!!! Você PERDEU!\n')
                break
        elif escolha in 'Pp':
            sleep(1)
            if soma % 2 == 0:
                print(f'\nVocê GANHOU!\n')
            else:
                print(f'\nDeu IMPAR!!! Você PERDEU!\n')
                break
        else:
            print('\nOpção Inválida. Deve digitar P ou I.\n')
        print(f'Vamos jogar novamente.\n')


def numero_extenso():
    for contador in range(0, 21):
        numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                   'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
                   'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
        numero = int(input('Digite um número de 0 a 20: '))
        print('-'*40)
        print('-'*40)
        if numero < 0 or numero > 20:
            continue
        else:
            print(f'O {numero} por extenso é {numeros[numero].upper()}\033[m.')
            print('-'*40)
            print('-'*40)
            opcao = str(input('Quer continuar(S/N): '))
            if opcao in 'Ss':
                continue
            elif opcao in 'Nn':
                print('-'*40)
                print('-'*40)
                print('Você parou.')
                print('-'*40)
                print('-'*40)
                break
            else:
                print('-'*40)
                print('-'*40)
                print('Opção inválida.')
                print('-'*40)
                print('-'*40)
                break


def sorteio_num():
    from random import randint
    print('-' * 20)
    print('Sorteio de números')
    print('-' * 20)

    numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
               randint(1, 10), randint(1, 10))
    print('Os valores sorteados foram: ', end='')
    for numero in numeros:
        print(f'{numero} ', end='')
    print(f'\n\nO maior número é {max(numeros)}')
    print(f'\nO menor número é {min(numeros)}')


def analise_numeros(numero):
    print('='*35)
    print(f'Você digitou os valores: {numero}')
    print('='*35)
    print(f'O valor 9 apareceu {numero.count(9)} vezes.')
    print('='*35)
    if 3 in numero:
        print(f'O valor 3 aparece na {numero.index(3)+1}ª posição.')
    else:
        print('Valor 3 não foi digitado.')
    print('='*35)
    for n in numero:
        if n % 2 == 0:
            print(f'Os valores pares digitados foram {n}')


def listar_maior_menor():
    numeros = list()
    for cont in range(0,5):
        numeros.append(int(input(f'Digite um número na posição {cont}: ')))
    print('='*50)
    print(f'Você digitou os valores {numeros}')
    print(f'\nO maior número é {max(numeros)} na posição {numeros.index(max(numeros))}.\n')
    print(f'O menor número é {min(numeros)} na posição {numeros.index(min(numeros))}.')
    print('\nFIM')


def valor_lista():
    numeros = list()
    while True:
        numero = (int(input('Digite um número: ')))
        if numero not in numeros:
            numeros.append(numero)
        else:
            print('Número já digitado.')
        pergunta = str(input('Quer continuar(S/N): ')).upper()
        print('\n')
        if pergunta in 'nN':
            break
        elif pergunta in 'Ss':
            continue
        else:
            print('A informação digitada é inválida.')

    numeros.sort()
    print(f'Os valores digitados são {numeros}')


def valor_metade(n, c=False):
    total = n / 2
    if c is True:
        return f'R${str(n).replace(".", ",")}'
    else:
        return f'{total:.2f}'


def listar_valores():
    numeros = list()
    for n in range(0, 5):
        numero = int(input('Digite um valor: '))
        if n == 0:
            numeros.append(numero)
        elif n > numeros[-1]:
            numeros.append(numero)
        else:
            posicao = 0
            while posicao < len(numeros):
                if numero <= numeros[posicao]:
                    numeros.insert(posicao, numero)
                    break
                posicao += 1
    print('+' * 30)
    print(f'Os valores digitados são {numeros}')


def extrair_lista():
    numeros = list()
    contador = int(1)
    while True:
        numeros.append(int(input('Digite um valor:')))
        pergunta = str(input('Quer continuar(S/N): '))
        if pergunta in 'nN':
            break
        contador += 1
    numeros.sort(reverse=True)
    print(f'\nForam digitados {contador} elementos.\n')
    print(f'Os valores da lista são {numeros}\n')
    if 5 in numeros:
        print('O valor 5 está na lista.')
    else:
        print('O valor 5 não está na lista.')


def dividir_lista():
    numeros = list()
    pares = list()
    impares = list()
    while True:
        numeros.append(int(input('Digite um número: ')))
        escolha = str((input('Quer continuar(S/N):').upper()))
        print('\n')
        if escolha in 'Nn':
            break
    for indice, valor in enumerate(numeros):
        if valor % 2 == 0:
            pares.append(valor)
        elif valor % 2 == 1:
            impares.append(valor)
    print('-' * 50)
    print(f'Os valores digitados são {numeros}')
    print(f'A lista de números pares é {pares}')
    print(f'A lista de números impares é {impares}')


def listar_par_impar():
    numero = [[],[]]
    valor = 0
    for contador in range(1,8):
        valor = int(input(f'Digite o {contador}º valor: '))
        if valor % 2 == 0:
            numero[0].append(valor)
        else:
            numero[1].append(valor)
    print('-=' * 30)
    numero[0].sort()
    numero[1].sort()
    print(f'Os valores pares digitados foram: {numero[0]}')
    print(f'Os valores impares digitados foram: {numero[1]}')


def matriz():
    m = [[0,0,0],[0,0,0],[0,0,0]]
    for linha in range(0,3):
        for coluna in range(0,3):
            m[linha][coluna] = str(input(f'Digite um nome: {[linha],[coluna]}: '))
    for linha in range(0,3):
        for coluna in range(0,3):
            print(f'[{m[linha][coluna]:^5}]', end='')
        print()


def matriz2():
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    somaPares = 0
    maior = 0
    somaColuna = 0
    for linha in range(0,3):
        for coluna in range(0,3):
            matriz[linha][coluna] = int(input(f'Digite um nome: {[linha],[coluna]}: '))
    print('-' * 30)
    for linha in range(0,3):
        for coluna in range(0,3):
            print(f'[{matriz[linha][coluna]:^5}]', end='')
            if matriz[linha][coluna] % 2 == 0:
                somaPares += matriz[linha][coluna]
        print()
    print('-' * 30)
    print(f'A soma dos valores pares é {somaPares}')
    for linha in range(0,3):
        somaColuna += matriz[linha][2]
    print(f'A soma dos valores da terceira coluna é {somaColuna}')
    for coluna in range(0,3):
        if coluna == 0:
            maior = matriz[1][coluna]
        elif matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
    print(f'O maior valor da segunda linha é {maior}')


def jogos_mega(quantidade):
    from random import randint
    from time import sleep
    lista = list()
    jogos = list()
    total = 1
    while total <= quantidade:
        contador = 0
        while True:
            numero = randint(1,60)
            if numero not in lista:
                lista.append(numero)
                contador += 1
            if contador >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        total += 1
    print('-=' * 3, f' SORTEANDO {quantidade} JOGOS', '-=' * 3)
    for indice, listas in enumerate(jogos):
        sleep(1)
        print(f'Jogo {indice + 1}: {listas}')


def calcular_area(largura, comprimento):
    soma = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {soma}m².')


def contador(i, f, p):
    from time import sleep
    print('-=' * 20)
    print(f'Contagenm de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ',end='', flush=True)#Para resolver o Buffer do Sleep
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('Fim!')


def valor_dobro(n, c=False):
    total = n * 2
    if c is True:
        return f'R${str(n).replace(".", ",")}'
    else:
        return f'{total:.2f}'


def fatorial2(num, show=False):
    """
    ---> Calcula do fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f'{c} X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


def leiaInt(mgs):
    ok = False
    valor = 0
    while True:
        n = str(input(mgs))
        if n.isnumeric():
            ok = True
            valor = int(n)
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
    return valor


def notas(*n, situacao=False):
    """
    ---> Funcão para analisar notas e situação de alunos
    :param n: Uma ou mais notas do aluno (aceita várias).
    :param situacao: Valor opcional, indica se deve ou não adicionar uma situação.
    :return: Dicionário com várias informações da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if situacao:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOÁVEL'
        else:
            r['situacao'] = 'RUIM'
    return r


def valor_aumenta(p, n, c=False):
    total = (n * (p / 100)) + n
    if c is True:
        return f'R${str(n).replace(".", ",")}'
    else:
        return f'{total:.2f}'


def valor_diminui(p, n, c=False):
    porcentagem = n * (p / 100)
    total = n - porcentagem
    if c is True:
        return f'R${str(n).replace(".", ",")}'
    else:
        return f'{total:.2f}'


def moeda(n):
    return f'R${str(n).replace(".", ",")}0'


def valor_resumo(n, a, r):
    dobra = n * 2
    metade = n / 2
    aumento = (n * (a / 100)) + n
    reducao = n - (n * (r / 100))

    return f'''
    ------------------------------------
             RESUMO DO VALOR
    ------------------------------------
    Preço analisado:\t\tR${moeda(n)}
    Dobro do preço:\t\t\tR${moeda(dobra)}
    Metade do preço:\t\tR${moeda(metade)}
    {a}% de aumento:\t\t\tR${moeda(aumento)}
    {r}% de redução:\t\t\tR${moeda(reducao)}
    ------------------------------------
    '''


def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Entrada "{entrada}" inválida, digite apenas números.')
        else:
            valido = True
            return float(entrada)


def leia_int(msg):
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


def leia_int2(i=0):
    return i


def leia_float(f=0):
    return f
