def media_aluno(n1, n2, n3, n4, n5):
    media = ((n1 + n2  + n3 + n4 + n5) / 5)
    return media


def lin():
    print('-' * 30)


lin()
print ("MEDIA DOS ALUNOS")
lin()

print("A media do primeiro aluno e:", media_aluno(1, 2, 3, 4, 5))
print("A media do segundo  aluno e:", media_aluno(6, 2, 7, 7, 8))
print("A media do terceiro aluno e:", media_aluno(5, 5, 3, 4, 5))
print("A media do quarto aluno e:", media_aluno(1, 10, 9, 9, 5))
print("A media do quinto aluno e:", media_aluno(8, 7, 6, 4, 5))

