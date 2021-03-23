def array_plus_array(arr1, arr2):
    soma1 = 0
    soma2 = 0
    soma_total = 0
    for i in arr1:
        soma1 = soma1 + i
    
    for ii in arr2:
        soma2 = soma2 + ii
    
    soma_total = soma1 + soma2
    print(soma_total)
        
arr1 = (1, 2)
arr2 = (1, 2)
array_plus_array(arr1, arr2)

