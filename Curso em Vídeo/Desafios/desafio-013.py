# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário atual: R$'))
aumento = salario * (1 + 0.15)

print('Seu salario de R${:.2f} passa a ser R${:.2f} após o aumento de 15%.'.format(salario, aumento))