aluguel = float(input('Quantos dias você usou o carro? '))
km = float(input('Quantos KM você andou no carro? '))
pagou = (aluguel * 60) + ( km * 0.15)



print('O total a pagar de diarias é R${:.2f}, e de KM R${:.2f} no total de R${:.2f}.'.format(aluguel * 60, km * 0.15, pagou))


#Forma do curso
dias = int(input('Quantos dias alugados?'))
km = int(input('Quantos km rodados?'))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
