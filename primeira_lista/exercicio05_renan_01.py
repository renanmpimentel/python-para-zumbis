preco = input("Digite o valor da mercadoria: ");
desconto = input("Valor do desconto (%): ");

valorDesconto = float(preco) * (float(desconto)/100);
print 'Valor do desconto: R$', valorDesconto;
print 'Valor a ser pago: R$', preco - valorDesconto;