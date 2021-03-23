def summation(num):
	contador = 0
	soma = 0
	while(contador < num):
		contador+=1
		soma+= contador
	return soma
	
print(summation(10))