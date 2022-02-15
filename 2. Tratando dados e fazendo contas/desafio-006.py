# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print('O número digitado foi {}. \nO dobro deste número é {}. \nO triplo deste número é {}. \nA sua raiz quadrada é {:.3f}.'.format(n, n*2, n*3, pow(n,(1/2))))
