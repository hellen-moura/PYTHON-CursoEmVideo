# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e
# milímetros. --> (km   hm   dam   m     dm     cm   mm)

medida = float(input('Digite uma distância em metros:'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {}m corresponde a:'.format(medida))
print('{:.1f} km'.format(km))
print('{:.2f} hm'.format(hm))
print('{:.3f} dam'.format(dam))
print('{:.0f} m'.format(m))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))