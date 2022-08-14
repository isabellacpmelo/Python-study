# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: R$'))
novo_preco = preco - (preco * 0.05)

print('O produto que custa R${:.2f} fica R${:.2f} com o desconto de 5%.'.format(preco, novo_preco))
