print("BOLETIM ESCOLAR")

nome = str(input("Insira o nome do aluno: "))
curso = str(input("Insira o curso do aluno: "))
semestre = str(input("Insira o semestre do aluno:"))
disciplina = str(input("Insira a disciplina: "))

nota1 = int(input("Insira a nota 1:"))
nota2 = int(input("Insira a nota 2:"))
media = int((nota1 + nota2) /2 )


print("RESULTADOS:")
print("NOME: ", nome)
print("CURSO: ", curso)
print("SEMESTRE: ", semestre)
print("DISCIPLINA:", disciplina)
print("NOTA 1: ", nota1)
print("NOTA 2:", nota2)

if(media > 59):
    print("Aprovado!")

elif(media < 40):
    print("Reprovado!")

else:
    print("Está de recuperação")
print("MEDIA:", media)
