def calculate():
    op = input('''
Escolha o tipo de operacao que voce deseja fazer:
+  Adicao
-  Subtracao
*  Multiplicacao
/  Divisao
0  SAIR    
    ''')
    if op == '0':
        exit()
    num_1 = float(input("Digite o primeiro numero: "))
    num_2 = float(input("Digite o segundo numero: "))

    if op == '+':
        print(num_1 + num_2)
    elif op == '-':
        print(num_1 - num_2)
    elif op == '*':
        print(num_1 * num_2)
    elif op == '/':
        print(num_1 / num_2)   
    else:
        print("Operacao invalida!")
    repete()
   
def repete():
    calc_repete = input('''
    Voce gostaria de calcular outro numero?
    Use S para SIM ou N para NAO!!    
    ''')

    if calc_repete.upper() == 'S':
        calculate()
    elif calc_repete.upper() == 'N':
        print("Ate Logo!")
    else:
        repete()


def stop():
    while True:
        break
calculate()