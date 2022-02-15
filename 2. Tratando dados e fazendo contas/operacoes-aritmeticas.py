# Aula sobre operações aritméticas
""" Ordem de Precedência
    1) ()
    2) **
    3) *, /, //, %
    4) +, -   """
print('-' * 30)    
nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('-' * 30)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2
rzn1 = n1 ** (1/2)
rzn2 = n2 ** (1/2)
print('A soma é {} \nA multipicação é {} \nA divisão é {} \nA divisão inteira é {} \nO resto é {} \nA potenciação é {}'.format(s, m, d, di, r, e))
print('A raiz de {} é {:.3f} e a raiz de {} é {:.3f}'.format(n1, rzn1, n2, rzn2))
print('-' * 30)
