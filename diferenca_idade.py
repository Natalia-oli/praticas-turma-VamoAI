def subtrair_idades (minha_idade, idade_mulher_steam):
    subtracao = idade_mulher_steam - minha_idade
    return print("A diferença entre minha idade e a idade de Margaret Hamilton é de {} anos!".format(subtracao))

def comparacao_estados(meu_estado, estado_margaret):
    if meu_estado.lower() == estado_margaret.lower():
        print("Somos pertencentes ao mesmo estado!")
    else:
        print("somos de estados diferentes!")

def comparacao_pais(meu_pais, pais_margaret):
    if meu_pais.lower() == pais_margaret.lower:
        print("Somos pertencentes ao mesmo pais!")
    else:
        print("Somos de paises diferentes!")

idade_natalia = int(input("Minha idade:"))
idade_steam = int(input("Idade de margaret"))
subtrair_idades(idade_natalia, idade_steam)

estado_natalia = input("meu estado e:")
estado_marg = input ("Estado da Margaret:")
comparacao_estados(estado_natalia, estado_marg)

pais_natalia = input("Meu pais e:")
pais_marg = input("Pais de Margaret")
comparacao_pais(pais_natalia, pais_marg)

if not 




