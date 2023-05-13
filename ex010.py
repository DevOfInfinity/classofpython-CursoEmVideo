#Trocando valores de moeda

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.99
euro = real / 5.46
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))