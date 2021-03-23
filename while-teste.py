def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

def sequence(n):
    while n != 1:
        print(n)
        if n % 2 == 0:        # n é par
            n = n / 2
        else:                 # n é ímpar
            n = n * 3 + 1
        
    
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')

# A condição do loop é True, que sempre é verdade, 
# então o loop roda até que chegue à instrução de interrupção.
# Esta forma de escrever loops while é comum porque podemos
# verificar a condição em qualquer lugar do loop 
# (não somente no topo) e podemos exprimir a 
# condição de parada afirmativamente (“pare quando isto acontecer”) 
# em vez de negativamente (“continue a seguir até que isto aconteça”).

condicao = False

if condicao == True:
    print("A condicao é verdadeira.")
else:
    print("A condicao é falsa.")
# A condicao é falsa.
# Note que fazer if condicao == True é equivalente a fazer if condicao,
# mas a segunda forma é mais usada. Talvez por ser mais sucinta,
# algumas pessoas costumam dizer que é um jeito mais "pythonico"
# de se escrever o código. Acostume-se com isso, pois você verá muito código escrito desse jeito