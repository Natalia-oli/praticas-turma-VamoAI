def divisoria():
    print("*" * 150)

def texto():

    print("As profissões ligadas a análises de dados estão cada vez mais em alta no mercado. Isso tem acontecido graças ao aumento da importância de tratar e interpretar os grandes fluxos de dados gerados pela sociedade. \n") 
    print("As análises de Big Data têm possibilitado que as empresas captem insights poderosos sobre seus consumidores, permitindo que elas tomem decisões estratégicas para seus negócios.  \n")
    print("O volume de dados gerado constantemente se tornou um dos principais desafios das empresas na atualidade. Portanto, elas passaram a depender, cada vez mais, de profissionais capacitados a realizarem todas as etapas de uma análise de dados - armazenar, separar, traduzir e fazer bom uso das informações. \n")

def espaco():
    print("\n")

def resultado(pontos_feitos):
    if (pontos_feitos > 0 ) and (pontos_feitos <= 62):
        print("Sua pontuação total foi {} e por isso, quando para o MM2 (MÓDULO 2)chegar, voce corre o risco de ficar perdido, então, foi derrotado pelo Modulo 1. PERDEU!".format(contador_pontos))
    elif (pontos_feitos > 63) and (pontos_feitos <= 70):
        print("Sua pontuação foi de {} e por isso, voce conseguiu driblar o MM1(MÓDULO 1), será bem sucedido na luta contra os outros módulos. VENCEU! PARABENS!".format(contador_pontos))
    elif pontos_feitos >= 71:
        print("Sua pontuação foi de {} e conseguiu vencer o MM1(MÓDULO 1) com perfeição. PARABENS! Foi uma otima performace!".format(contador_pontos))
    elif pontos_feitos < 0:
        print("Sua pontuação foi de {} e por isso voce foi infinitamente derrotado pelo MM1 (MÓDULO 1)".format(contador_pontos))
    else:
        print("")

#variaveis
contador_pontos = 0 
#PARTE 1 - VISUAL
espaco()
espaco()
divisoria()
print("TRILHA DO PROFISSIONAL- ANALISE DE DADOS - MODULO 1")
divisoria()
print("2021 - #VAMOAI - RESILIA E IFOOD")
divisoria()
texto()

#PARTE 2 - AVATARES
print("Diante desse cenário dos dados. Você passará por uma jornada, que será composta pPara fazer essa trilha é necessário escolher quem você quer ser nessa jornada.")
print("1 - O ser que faz as coisas sempre no último segundo - poster \n 2 - Está sempre disponível e disposto a ajudar e tenta cumprir tudo no prazo - onipresente \n 3 - O 'deixa a vida me levar e faz do jeito que dá certo' - ondestou  \n 4 - Oferece o máximo de si, apesar das circuntâncias - esformax")
espaco()

#IDENTIFICANDO AVATAR ESCOLHIDO PELO NOME
avatar = int(input("Digite o nuúmero referente a sua escolha de avatar:"))
if avatar == 1:
    print ("Olá, Poster, nessa trilha para alcançar a formação plena com enfâse na análise de dados, voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos telões e respondendo com sinceridade :).  Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló,suas respostas são as armas e depende de você, elas serem poderosas ou não!:) \n  BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO VAI LHE LEVAR!\n ")
elif avatar == 2:
    print ("Olá, onipresente, nessa trilha para alcançar a formação plena com enfâse na análise de dados, voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos telões e respondendo com sinceridade :).  Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló,suas respostas são as armas e depende de você, elas serem poderosas ou não!:). \n  BOA SORTE! AO FINAL, SABEREMOS ONDE SEU PERCURSO VAI LHE LEVAR!\n")
elif avatar == 3:
    print ("Olá, ondestou, nessa trilha para alcançar a formação plena com enfâse na análise de dados, voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos telões e respondendo com sinceridade. Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló,suas respostas são as arcas e depende de você, elas serem poderosas ou não!:)   \n AO FINAL, SABEREMOS ONDE SEU PERCURSO VAI LHE LEVAR!\n ")
elif avatar == 4:
    print ("Olá, esformax, nessa trilha para alcançar a formação plena com enfâse na análise de dados, voce passará por um corredor com algumas salas e entrará em cada uma, lendo as perguntas dos telões e respondendo com sinceridade :).  Há um monstro invisivel, chamado de MM1(Mostro Módulo 1), para derrota-ló,suas respostas são as arcas e depende de você, elas serem poderosas ou não!:) \n AO FINAL, SABEREMOS ONDE SEU PERCURSO VAI LHE LEVARE! \n ")
divisoria()

espaco()

#DESDOBRAMENTOS DE ACORDO COM O AVATAR 
if (avatar == 1) or (avatar == 2) or (avatar == 3) or (avatar == 4):
    modulo1 = int(input("Você entrou em uma sala chamada de SALA TECH|SOFT com uma tela com a seguinte frase exposta:\n- VOCE SENTE QEUE APRENDEU TODOS OS CONCEITOS|CONTEÚDOS DE SOFT E TECH DO MÓDULO 1?\n (1) - SIM \n (2) - NÃO, DEIXEI DE COMPREENDER ALGUNS|ALGUM:"))
    if modulo1 == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE ADQUIRIU {} PONTOS E ESTÁ MAIS FORTE PARA DERROTAR O MM1!".format(contador_pontos))
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE JÁ COMEÇOU PERDEU 10 PONTOS: {} E POR ISSO PRECISARÁ IR PARA A SALA DO REFORÇO, REVISAR PARA CHEGAR MAIS FORTE AO MM2!".format(contador_pontos))
               
  
    ajuda = int(input("Agora, a próxima é a SALA DA AJUDA. O telão exibe a pergunta:\n-VOCE AJUDOU ALGUÉM, DE ALGUMA MANEIRA, DURANTE O MÓDULO 1?\n (1) - SIM \n (2) - NÃO:"))
    if ajuda == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
        print("DEVIDO ISSO, TORNOU-SE MAIS FORTE NO CONCEITO SOFT SKILSS! AS EMPRESAS GOSTAM!")
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
        print("REFLITA SOBRE A IMPORTÂNCIA DO TRABALHO E EVOLUÇÃO EM GRUPO , QUANDO ENSINAMOS APRENDEMOS.\n DIRIJA-SE A SALA DA AJUDA!")
        for i in range (1, 5):
            print("aprendendo sobre a importancia da evolução em grupo: {} dia".format(i))
            
    monitoria = input("A próxima sala é a SALA DA MONITORIA, que apresenta a seguinte pergunta:\n -VOCE PARTICIPOU DAS MONITORIAS ?  \n (1) - ENTRE 1 E 3 MONITORIAS \n (2) - ENTRE 4 - 6 \n (3)- MAIS DE 7 \n (4) - NENHUMA DAS ALTERNATIVAS:")
    if monitoria == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! AGORA VOCE ESTA COM:{} PONTOS".format(contador_pontos))
    elif monitoria == 2:
        contador_pontos = contador_pontos + 20
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    elif monitoria == 3: 
        contador_pontos = contador_pontos + 30
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    elif monitoria == 4:
        contador_pontos = contador_pontos - 10
        print( "VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    else:
        print("Digite um dos numeros indicados")
    
    curso_alura = int(input("Seguindo nas salas,a próxima é a SALA DA ALURA, com a seginte pergunta: \n -VOCE FEZ ALGUM CURSO COMPLETO NA ALURA?:\n (1) - SIM, UM OU MAIS DE UM \n (2) - NÃO, NENHUM:"))
    if curso_alura == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
    else:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))

    falta_aulas = int(input("A  próxima sala é a SALA DAS FALTAS:\n - QUANTAS AULAS FALTOU ATÉ O MOMENTO?"))
    if falta_aulas >= 4:
        print("VOCE PERDEU! É NECESSÁRIO TER AO MENOS 80% DE PRESENÇA NO MÓDULO PARA DERROTAR O MOSTRO!")
    else:
        contador_pontos = contador_pontos + 5
        ("AGORA VOCE ESTÁ COM {}".format(contador_pontos))

    atividades_qualified = int(input("Agora é a SALA DO QUALIFIED: \n - DEIXOU DE ENVIAR QUANTAS ATIVIDADES DO QUALIFIED?\n (1)- NENHUMA, TODAS ENVIADAS \n (2)- MAIS DE UMA  (3) - MAIS DE 3:"))
    if atividades_qualified == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
    elif atividades_qualified == 2:
        contador_pontos = contador_pontos - 7
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    elif atividades_qualified == 3:
        print("VOCE FOI DERROTADO PELO MM1, POIS DEIXAR DE ENVIAR MAIS DE TRÊS ATIVIDADES FORTALECE ELE E LHE ENFRAQUECE!")
    
    atividades_pdf = int(input("A outra pergunta realizada está na SALA DOS PDFS: \n - ATÉ AQUI, VOCE CONSUMIU TUDO ENVIADO NOS PDFS? \n (1) - SIM \n (2) - NÃO, \n (3) - MAIS OU MENOS:"))
    if atividades_pdf == 1:
        contador_pontos = contador_pontos + 10
        print("PARABENS! VOCE AGORA ESTA COM {} PONTOS!".format(contador_pontos))
    elif atividades_pdf == 2:
        contador_pontos = contador_pontos - 10
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    elif atividades_pdf == 3:
        contador_pontos = contador_pontos + 4
        print("VOCE AGORA ESTA COM {} PONTOS".format(contador_pontos))
    else:
        print("Digite um número válido!")

else:
    print("DIGITE UM NUMERO VÁLIDO!")

#CHAMADA DA FUNÇÃO QUE VAI APRESENTAR O RESULTADO DO JOGO
pontos_feitos = contador_pontos
resultado(pontos_feitos)





    

  
    
        

    


