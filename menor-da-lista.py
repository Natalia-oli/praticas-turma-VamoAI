def find_smallest(numbers):
    menor = 0
    for numero in numbers:
        if numero < menor:
            menor = numero
    print(menor)

numbers = [8, -9, 2]
find_smallest(numbers)