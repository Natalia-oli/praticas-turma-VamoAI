def complete_series(seq):
    nova_lista = list()
    maior = seq[0]
    repetido = False
    for num1 in seq:
        for num2 in seq:
            if (num1 == num2):
                repetido = True
    if repetido == True:
        print(0)
    
    for numero in seq(0, maior):
        nova_lista.append(numero)
        print(nova_lista)
      

seq = (4, 1, 8, 5, 6, 7)
complete_series(seq)