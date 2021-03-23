def ordena_dicionario(dicionario):
  menor = 0
  nova_lista = {}
  
  if dicionario == {}:
    return {}
  
  else:
    for kys in dicionario.keys():
      for valor in dicionario.values():
        if valor <= menor:
          nova_lista[kys] = menor
        return nova_lista

dicionario = {'a': 2, 'b': 1, 'c': 3}
ordena_dicionario(dicionario)