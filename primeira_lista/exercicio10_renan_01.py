#!/usr/bin/python
cigarros = input("Quantos cigarros voce fuma por dia: ");
anos = input("Quantos anos voce ja eh fumante: ");

cadaCigarro = 10;

totalCigarros = cadaCigarro * int(cigarros);
totalDiasPerdidos = (totalCigarros * int(anos)) / 1440;

if(totalDiasPerdidos > 1):
	print 'Voce ja perdeu: ', float(totalDiasPerdidos), 'dias';
else:
	print 'Voce nao perdeu nem um dia de vida ainda'; 