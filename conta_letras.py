def conta_letras(string):
  dicionario_keys = {}
  for letra in string:
    repetidas = string.count(letra)
    dicionario_keys[letra] = repetidas
  return dicionario_keys

string = "aAb"
conta_letras(string)
    