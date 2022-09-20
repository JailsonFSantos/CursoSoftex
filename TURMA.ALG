Algoritmo "Turma"

Var

r1: caractere
cont, apvd: inteiro
aluno, ma: caractere
n, melhor_n: Real


Inicio
      Repita
            Escreval("Digite a Turma:")
            leia(r1)
            se r1 = "A" entao
               escreval("Cadastro da Turma 'A'.")
            senao
                 se r1 = "B" entao
                    escreval("Cadastro da Turma 'B'.")
                 senao
                      se r1 = "C" entao
                         escreval("Cadastro da Turma 'C'.")
                      senao
                           se r1 = "D" entao
                              escreval("Cadastro da Turma 'D'.")
                           fimse
                      fimse
                 fimse
            fimse
            
            
            cont <- 1
            apvd <- 0
            melhor_n <- 0
            
            para cont de 1 ate 25 faca
                 Escreval("Aluno", cont)
                 escreval("Qual o nome do Aluno?")
                 leia(aluno)
                 escreval("Qual a nota de ", aluno, "?")
                 leia(n)
                 
                 se n > melhor_n entao   //se nova nota for maior
                    melhor_n <- n        //Melhor nota recebe nota
                    ma <- aluno          // e melhor aluno recebe aluno novo!
                 fimse

                 se n >= 7 entao
                    escrevaL("Aluno foi aprovado")
                    apvd <- apvd + 1
                 senao
                 escrevaL("Aluno foi reprovado!")
                 fimSe

            fimpara
            
            Escreval("Deseja Cadastra outra turma? [S/N]")
            leia(r1)
      ate (r1 = "N")
      
      
      Escreval("O Total de aprovados foi de: ", apvd.)
      Escreval("O Aluno com maior nota foi: ", ma, " com a nota: ", melhor_n.)
            
                 
                 
               



Fimalgoritmo