from ast import Break
from distutils.command.sdist import sdist
from mailbox import linesep
from pickle import TRUE
from time import sleep
from rich import print
import os


VOTOS_CAD01 = 0
VOTOS_CAD02 = 0
VOTOS_CAD03 = 0
VOTOS_NULOS = 0

while True:

    print('*' *20)
    print(f"TOTAL CANDIDATO 1: {VOTOS_CAD01}{os.linesep}TOTAL CANDIDATO 2: {VOTOS_CAD02}{os.linesep}TOTAL CANDIDATO 3: {VOTOS_CAD03}{os.linesep}TOTAL VOTOS NULOS: {VOTOS_NULOS}{os.linesep} ")
    print('*' *20)

    try:
                
        voto = int(input(f"Digite o numero do seu candidato:{os.linesep}889 - Candidato-1{os.linesep}847 - Candidato-2{os.linesep}515 - Candidato-3{os.linesep} Seu Voto: "))

        if voto == 889:
            VOTOS_CAD01 += 1
        elif voto == 847:
            VOTOS_CAD02 += 1
        elif voto == 515:
            VOTOS_CAD03 += 1
        else:
            VOTOS_NULOS += 1        

    except:
        print("Opcao Invalida!!")
        sleep(3)

    parar =input("Voce Gostaria de encerrar? [S]/[N]") 
    if parar == 'S':
        if VOTOS_CAD01 > VOTOS_CAD02 and VOTOS_CAD01 > VOTOS_CAD03:
            print(f"Candidato1 teve: {VOTOS_CAD01} votos, Candidato2 teve: {VOTOS_CAD02} votos, Candidato3 teve: {VOTOS_CAD03} votos, Votos Nulos: {VOTOS_NULOS} votos!")
            print(f"O Vencedor foi o candidato 1 com: {VOTOS_CAD01} VOTOS!!")
        elif VOTOS_CAD02 > VOTOS_CAD01 and VOTOS_CAD02 > VOTOS_CAD03:
            print(f"Candidato1 teve: {VOTOS_CAD01} votos, Candidato2 teve: {VOTOS_CAD02} votos, Candidato3 teve: {VOTOS_CAD03} votos, Votos Nulos: {VOTOS_NULOS} votos!")
            print(f"O Vencedor foi o candidato 2 com: {VOTOS_CAD02} VOTOS!!")
        elif VOTOS_CAD03 > VOTOS_CAD02 and VOTOS_CAD03 > VOTOS_CAD01:
            print(f"Candidato1 teve: {VOTOS_CAD01} votos, Candidato2 teve: {VOTOS_CAD02} votos, Candidato3 teve: {VOTOS_CAD03} votos, Votos Nulos: {VOTOS_NULOS} votos!")
            print(f"O Vencedor foi o candidato 3 com: {VOTOS_CAD03} VOTOS!!")
        else:
            print("Nao houve ganhador!")
        sleep(60)
        break
        
    else:
        pass

        
os.system('cls')


        


