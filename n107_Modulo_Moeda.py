from utilidades import numeros

valor = float(input('Digite o preço(R$): '))
print(f'A metade de {valor:.2f} é {numeros.valor_metade(valor)}')
print(f'O dobro de {valor:.2f} é {numeros.valor_dobro(valor)}')
print(f'Aumentando 15%, o total será {numeros.valor_aumenta(15, valor)}')
print(f'Reduzindo 13%, o total será {numeros.valor_diminui(13, valor)}')