Algoritmo "Adivinhar"

Var

r1,r2,r3,r4,r5,r6,r7,r8,r9: caractere
r11,r12,r13,r14,r15,r16,r17,r18,r19: caractere
r21,r22,r23,r24,r25,r26,r27,r28,r29: caractere

Inicio

Escreval("************Bem vindo ao Jogo da Adivinhacao.***************")
Escreval("Escolha um VEICULO na lista abaixo:")
Escreval("Trator-Moto-Bicicleta-Trem-Carro-Caminhão-Ônibus-Paraquedas,")
Escreval("Balão-Avião-Helicóptero-Submarino-Barco-Navio-Lancha.")
Escreval("Escolha a Numero de 1 a 3 da opcao Correspondente abaixo.")
Escreval("Em seguida responda as perguntas com apenas 'sim' ou 'nao'")
Escreval("Lembrando que respostas diferentes anularao o jogo!")
Escreval("VAMOSS LAA!!!")
Escreval("1-Terrestre, 2-Aereo ou 3-Aquatico!!")
leia(r1)
escolha r1
caso "1"
       escreval("Cabe apenas uma pessoa?")
       leia(r2)
       se r2 = "sim" entao
          escreval("É pesado?")
          leia(r3)
          se r3 = "sim" entao
             escreval("Trator!")
          senao
               escreval("Tem pedal?")
               leia(r4)
               se r4 = "sim" entao
                  escreval("Bicicleta!")
               fimse
          fimse
       senao
            escreval("Usa capacete?")
            leia(r5)
            se r5 = "sim" entao
               escreval("Moto!")
            senao
                 escreval("Tem passageiro?")
                 leia(r6)
                 se r6 = "sim" entao
                    escreval("Usa trilho?")
                    leia(r7)
                    se r7 = "sim" entao
                       escreval("Trem!")
                    senao
                         escreval("Anda na pista?")
                         leia(r8)
                         se r8 = "sim" entao
                            escreval("É veiculo leve?")
                            leia(r9)
                            se r9 = "sim" entao
                               escreval("Carro!")
                            senao
                                 escreval("É alto?")
                                 leia(r11)
                                 se r11 = "sim" entao
                                    escreval("Usa carroceria?")
                                    leia(r12)
                                    se r12 = "sim" entao
                                       escreval("Caminhao!")
                                 senao
                                      escreval("Pode ter cobrador?")
                                      leia(r12)
                                      se r12 = "sim" entao
                                         escreval("Onibus!")
                                      fimse
                                    fimse
                                 fimse
                            fimse
                         fimse
                    fimse
                 fimse
            fimse
       fimse
       
       
       
       
       
caso "2"
       escreval("Precisa pular?")
       leia(r13)
       se r13 = "sim" entao
          escreval("Asa delta!")
       senao
            escreval("Viaja dentro?")
            leia(r14)
            se r14 = "sim" entao
               escreval("É devagar?")
               leia(r15)
               se r15 = "sim" entao
                  escreval("Balao!")
               senao
                    escreval("Tem piloto?")
                    leia(r16)
                    se r16 = "sim" entao
                       escreval("Possui asas fixas?")
                       leia(r17)
                       se r17 = "sim" entao
                          escreval("Aviao!")
                       senao
                            escreval("Faz voo vertical?")
                            leia(r18)
                            se r18 = "sim" entao
                               escreval("Helicoptero!")
                            fimse
                       fimse
                    fimse
               fimse
            fimse
       fimse
       
       
       
       

outrocaso
         escreval("É coberto de agua?")
         leia(r19)
         se r19 = "sim" entao
            escreval("Submarino!")
         senao
              escreval("Navega na agua?")
              leia(r21)
              se r21 = "sim" entao
                 escreval("Possui velas?")
                 leia(r22)
                 se r22 = "sim" entao
                    escreval("Barco!")
                 senao
                      escreval("Tem motor?")
                      leia(r23)
                      se r23 = "sim" entao
                         escreval("É alto?")
                         leia(r24)
                         se r24 = "sim" entao
                            escreval("Navio!")
                         senao
                              escreval("Pode ser descoberto?")
                              leia(r25)
                              se r25 = "sim" entao
                                 escreval("Lancha!")
                              fimse
                         fimse
                      senao
                      fimse
                 fimse
              fimse
         fimse
         
         
         
         
fimescolha

Fimalgoritmo