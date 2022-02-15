# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m*1000

print('O valor escolhido foi {:.1f} m, que em centímentros fica {:.1f} cm e em milímetros fica {:.1f} mm.'.format(m, cm, mm))

