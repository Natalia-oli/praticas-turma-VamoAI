def verifica_chave(dicionario, chave):
   if dicionario == {}:
      return False
    
   else:
    for k in dicionario.keys():
      if k in chave:
        return True
      else:
        return False
      