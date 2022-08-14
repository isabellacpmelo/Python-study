# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a a sua média.

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
soma = (nota1 + nota2)
media = soma/2

print('As notas do aluno foram {} e {}, sua soma é {} e a média {}.'.format(nota1, nota2, soma, media))

