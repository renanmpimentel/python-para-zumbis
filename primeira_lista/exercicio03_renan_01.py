#!/usr/bin/python
dias = input("Digite os dias: ");
horas = input("Digite as horas: ");
minutos = input("Digite os minutos: ");
segundos = input("Digite os segundos: ");

segundosMinuto = 60;
segundosHoras = 60 * segundosMinuto;
segundosDia = 24 * segundosHoras;

totalSegundo = (dias*segundosDia) + (horas*segundosHoras) + (minutos*segundosMinuto) + segundos;

print totalSegundo, 'segundos';