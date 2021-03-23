def complete_series(seq):
    l = ()
    i = 0
    maior = seq[0]
    for numero in seq:
        if numero > maior:
            maior = numero
            for i in range(0, maior):
                i += i
                l.append(i)
            l.sort()
            print(l)
    
   
        

seq = (4, 1)
complete_series(seq)