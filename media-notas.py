nota1 = float(input(" Digite sua nota de matematica:"))

nota2 = float(input(" Digite sua nota de portugues:"))
nota3 = float(input(" Digite sua nota de ingles:"))

media = ((nota1 + nota2 + nota3) / 3)

if media >= 6:
    print("Voce esta aprovado :)")

else:
    print ("Reprovado :/")