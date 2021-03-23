produto1 = input("Digite o nome do produto 1:")
preco1 = float(input("Digite o valor do produto 1:"))

produto2 = input("Digite o nome do produto 2:")
preco2 = float(input("Digite o valor do produto 2:"))

produto3 = input("Digite nome produto 3:")
preco3 = float(input("Digite o valor do produto 3:"))

if preco1 < preco2 and preco1 < preco3:
    print("o produto mais barato e a(o)", produto1)

elif preco2 < preco1 and preco2 < preco3:
    print("O produto mais barato da loja e a(o):", produto2)

elif preco3 < preco1 and preco3 < preco2:
    print ("O produto mais barato da loja e a(o):", produto3)
else: 
    print ("Os tres apresentam o mesmo valor!")
