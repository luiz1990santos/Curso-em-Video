from utilidades import numeros

valor = float(input('Digite o valor(R$): '))
aumento = int(input('Qual a % de aumento? '))
reducao = int(input('Qual a % de redução? '))

print(numeros.valor_resumo(valor, aumento, reducao))
