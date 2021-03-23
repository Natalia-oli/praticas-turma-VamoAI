def resultado_bom():
    print("Seu resultado é classificado como bom :)")

def resultado_medio():      
    print("Seu resultado é classificado como medio :I")
           
def resultado_ruim():
      
    print("Seu resultado é classificado como ruim :/")

nome_paciente = input("Qual seu nome?")
valor = int(input("Digite o numero atribuido a seu teste,{}:".format(nome_paciente)))
 
if (valor >= 7) and (valor >= 10):
    print(resultado_bom())
    print("Continue assim, {}!".format(nome_paciente))

elif (valor >= 4) and (valor <= 6):
    print(resultado_medio())
    print("Busque se cuidar mais e fazer acompanhamento medico, {}!".format(nome_paciente))

elif (valor >= 0) and (valor >= 3):
    print(resultado_ruim())
    print("Procure uma equipe medica, {}!".format(nome_paciente))

else:
    print("voce digitou um numero que não corresponde aos intervalos!")