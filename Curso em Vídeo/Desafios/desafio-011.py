# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m^2'.format(larg, alt, area))
print('Para pintar essa parede você precisará de {}l de tinta.'.format(tinta))
