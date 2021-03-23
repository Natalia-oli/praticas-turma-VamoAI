padrao = 35
vip = 60
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if (idade >= 18):
  alunx = int(input("Estudante de python, digite 1. Se não for, digite 0: "))
  opcoes = int(input("Entrada padrao: R$35,00 - digite 1. Entrada vip: R$60,00 - digite 2: "))
  if (alunx == 1) and (opcoes == 1):
    porc_padrao = padrao * (50/100)
    print("Voce está apta(o) para adquirir o ingresso padrao e tera um desconto de 50%. Valor final: {}".format (porc_padrao))
  elif (alunx == 1) and (opcoes == 2):
    porc_vip = vip * (60/100)
    print("Voce está apta(o) para adquirir o ingresso VIP e tera um desconto de 50%. Valor final: {}".format (porc_vip))
  elif (alunx == 0) and (opcoes == 1):
    print('Preço a pagar: ', padrao)
  elif (alunx == 0) and (opcoes == 2):
    print('Preço a pagar: ', vip)
else:
  falta_idade = 18 - idade
  print('Você ainda é de menor: falta {} anos para você ser de maior e ter acesso ao clube'.format (falta_idade))