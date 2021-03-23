def soma_valores(dicionario):
  soma = 0
  for valores in dicionario.values():
    soma += valores
    return soma
    

dicionario = {'a':1, 'b':2}
soma_valores(dicionario)
   