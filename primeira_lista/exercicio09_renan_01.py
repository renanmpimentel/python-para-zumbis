#!/usr/bin/python
dias = input("Digite o total de dias: ");
km = input("Digite o total de km: ");

totalDias = int(dias)*60;
totalKm = float(km)*0.15;

print 'O valor a ser pago: ', totalDias+totalKm;