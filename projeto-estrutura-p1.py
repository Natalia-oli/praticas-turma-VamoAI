def divisoria():
    print("*" * 60)

def texto():

    print("As profissões ligadas a análises de dados estão cada vez mais em alta no mercado. Isso tem acontecido graças ao aumento da importância de tratar e interpretar os grandes fluxos de dados gerados pela sociedade. \n") 
    print("As análises de Big Data têm possibilitado que as empresas captem insights poderosos sobre seus consumidores, permitindo que elas tomem decisões estratégicas para seus negócios.  \n")
    print("O volume de dados gerado constantemente se tornou um dos principais desafios das empresas na atualidade. Portanto, elas passaram a depender, cada vez mais, de profissionais capacitados a realizarem todas as etapas de uma análise de dados - armazenar, separar, traduzir e fazer bom uso das informações. \n")

def espaco():
    print("\n")

#PARTE 1 - VISUAL

divisoria()
print("TRILHA DO PROFISSIONAL- ANALISE DE DADOS - MODULO 1")
divisoria()
print("2021 - #VAMOAI - RESILIA E IFOOD")
divisoria()
texto()

#PARTE 2 - AVATARES
divisoria()
print("Para fazer essa trilha é necessário escolher quem você quer ser nessa jornada.")
print("1 - O ser que faz as coisas sempre no último segundo - procrastinador \n 2 - Está sempre disponível e disposto a ajudar e tenta cumprir tudo no prazo - onipresente \n 3 - O 'deixa a vida me levar e faz do jeito que dá certo' - ondestou  \n 4 - Oferece o máximo de si, apesar das circuntâncias - esformax")
espaco()
avatar = int(input("Digite o nuúmero referente a sua escolha de avatar:"))

divisoria()
espaco()

#DESDOBRAMENTOS DE ACORDO COM O AVATAR 

if avatar == 1:
    print ("Nessa trilha para alcançar a formação plena com enfâse na análise de dados é necessário fazer escolhar, renúncias e assim projetar o futuro com base no presente. Agora chegou o momento de fazer escolhas!")
    modulo1 = int(input("Você entrou em uma sala chamada de SALA TECH|SOFT com uma tela com a seguinte frase exposta:\n- VOCE SENTE QEUE APRENDEU TODOS OS CONCEITOS|CONTEÚDOS DE SOFT E TECH DO MÓDULO 1?\n (1) - SIM \n (2) - NÃO, DEIXEI DE COMPREENDER ALGUNS|ALGUM:"))
    if modulo1 == 1:
        print("PARABENS! VOCE ADQUIRIU 10 PONTOS!")
    else:
        print("VOCE JÁ COMECOU PERDENDO 10 PONTOS!")

    ajuda = int(input("Agora, a próxima é a SALA DA AJUDA. O telão exibe a pergunta:\n-VOCE AJUDOU ALGUÉM, DE ALGUMA MANEIRA, DURANTE O MÓDULO 1?\n (1) - SIM \n (2) - NÃO:"))
    if ajuda == 1:
        print("PARABENS! VOCE CONSEGIUIU MAIS 10 PONTOS!")
    else:
        print("VOCE PERDEU 10 PONTOS!")

    monitoria = int(input("A próxima sala é a SALA DA MOMITORIA, que apresenta a seguinte pergunta:\n -VOCE PARTICIPOU DAS MONITORIAS: (1) - ENTRE 1 E 3 MONITORIAS \n (2) - ENTRE 4 - 6 \n (3)- MAIS DE 7 \n (4) - NENHUMA DAS ALTERNATIVAS:"))
    if monitoria == 1:
        print("PARABENS! VOCE GANHOU MAIS 10")
    elif monitoria == 2:
        print("PARABENS! VOCE GANHOU MAIS 20 PONTOS!")
    elif monitoria == 3: 
        print("PARABENS! VOCE GANHOU MAIS 30 PONTOS!")
    elif monitoria == 4:
        print( "VOCE PERDEU MAIS 10 PONTOS!")
    else:
        print("Digite um dos numeros indicados")
    
    curso_alura = int(input("Seguindo nas salas,a próxima é a SALA DA ALURA, com a seginte pergunta: \n -VOCE FEZ ALGUM CURSO COMPLETO NA ALURA?:\n (1) - SIM, UM OU MAIS DE UM \n (2) - NÃO, NENHUM:"))
    if curso_alura == 1:
        print("PARABENS! VOCE GANHOU MAIS 10 PONTOS!")
    else:
        print("VOCE PERDEU 10 PONTOS!")

    falta_aulas = int(input("A  próxima sala é a SALA DAS FALTAS:\n - FALTOU EM ALGUMA AULA ATÉ O MOMENTO? \n (1) - SIM \n (2)- NÃO:"))
    if falta_aulas == 1:
        print("PARABENS! VOCE GANHOU MAIS 10 PONTOS!")
    else:
        print("VOCE PERDEU 10 PONTOS!")

    atividades_qualified = int(input("Agora é a sala do qualified: \n - ENVIOU TODAS AS ATIVIDADES DO QUALIFIED \n (1)- SIM \n (2)- NÃO:"))
    if atividades_qualified == 1:
        print("PARABENS! VOCE GANHOU MAIS 10 PONTOS!")
    else:
        print("VOCE PERDEU 10 PONTOS!")
    
    atividades_pdf = int(input("A outra pergunta realizada na sala atual é SALA DOS PDFS: \n - ATÉ AQUI, VOCE CONSUMIU TUDO ENVIADO NOS PDFS \n (1) - SIM \n (2) - NÃO, \n (3) - MAIS OU MENOS:"))
    if atividades_pdf == 1:
        print("PARABENS! VOCE GANHOU MAIS 10 PONTOS!")
    elif atividades_pdf == 2:
        print("VOCE PERDEU 10 PONTOS!")
    elif atividades_pdf == 3:
        print("VOCE GANHOU 4 PONTOS!")
    else:
        print("Digite um número válido!")
else:
    print("DIGITE UM NUMERO VÁLIDO!")

    

  
    
        

    


