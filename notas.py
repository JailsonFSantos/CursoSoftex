print("****Sistema de Avaliacao do Aluno!****")


nome = input("Qual nome do Aluno(a)?\n")
faltas = int(input("Quantas faltas ele(a) teve no periodo?\n"))
nota_1 = float(input("Qual a primeira nota?\n"))  
nota_2 = float(input("Qual a segunda nota?\n"))
nota_fim = (nota_1 + nota_2) /2

if faltas >= 3:
    print(f"O aluno {nome} Foi Reprovado por falta!")
elif nota_fim < 7:
    print(f"O aluno{nome} Foi Reprovado com nota:","%.2f" % nota_fim)
else:
    print(f"O aluno {nome} Foi Aprovado com nota:","%.2f" % nota_fim)