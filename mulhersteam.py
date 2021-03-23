acertou = 0
pergunta1 = int(input("Escolha 2 dentre as opcoes abaixo: Matgaret Hamilton é: 1 - mulher. 2 - programadora. 3- homem: "))
pergunta2 = int(input("Quais materias essa Matgaret lecionou para o ensino medio: 1 - Frances. 2 - Matematica. 3 - Fisica: "))
pergunta3 = int(input("Margaret desenvolveu quais conceitos: 1- computacao parelela. 2 - teste de sistema. 3 - Inteligencia Artificial: "))

if pergunta1 == 1 or pergunta1 == 2:
  print("acertou a primeira pergunta")
  acertou += 1
else:
  print("Errou a primeira")

if pergunta2 == 1 or pergunta2 == 2:
  print("acertou a segunda pergunta")
  acertou += 1
else:
  print('Errou a segunda')

if pergunta3 == 1 or pergunta3 == 2:
  print("acertou a terceira pergunta")
  acertou += 1
else:
  print('Errou a terceira')

print ("Voce acertou{} questoes".format(acertou))
print('Matgaret Hamilton foi uma mulher, programadora, lecionou no ensino médio as disciplinas de Frances e Matemática e desenvolveu conceitos de computação paralela e teste de sistema')



