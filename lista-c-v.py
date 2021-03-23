def conta_letras(string):
  total = len(string)
  contador = 0
  dicionario_keys = {}
  for letra in string:
    while contador < total:
      contador += contador
      dicionario_keys[letra] = contador
  return dicionario_keys

string = "abc"
conta_letras(string)