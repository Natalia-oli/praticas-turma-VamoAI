def procura_chave_na_lista(dicionario):
  novo_dicionario = {}
  
  if dicionario == {}:
    return {}

  else:
    for k in dicionario.keys():
      for v in dicionario.values():
        if k == v:
          verdade = True
          novo_dicionario[k] = verdade
        elif  k != v:
          falso = False
          
        else:
          falso = False
          novo_dicionario[k] = falso
        return novo_dicionario
          
dicionario = {"a": ["a", "b", "c"], "b": [1, 2, 3, "b"]}
procura_chave_na_lista(dicionario)