#!/usr/bin/python
salario = input("Digite o salario atual: ");
aumento = input("Digite a porcentagem do aumento: ");

valorAumento = float(salario) * (float(aumento)/100);
print 'Valor do aumento: R$', float(valorAumento);
print 'Valor do novo salario: R$', valorAumento+salario; 