def lista_para_dicionario(lista):
  a = []
  b = []
  for k in lista:
    a.append(k)
    
  for v in lista:
    b.append(v)
    
  dicionario = dict(zip(a, b))
  return dicionario
    
lista = [1, 2, 3]
lista_para_dicionario(lista)