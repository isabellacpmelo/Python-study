# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$3,27

real = float(input('Digite quanto você possui em sua carteira: R$'))
dolar = real / 3.27

print('Com o valor de R${:.2f}, você pode comprar US${:.2f}.'.format(real, dolar))
