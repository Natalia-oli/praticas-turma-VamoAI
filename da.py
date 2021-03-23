def positive_sum(arr):
    quantidade_numeros = len(arr)
    soma = 0
    for n in arr:
        if n >= 0:
            soma += n
    return(soma)
    
arr = (1, 2, 5, -4, -6)
positive_sum(arr)