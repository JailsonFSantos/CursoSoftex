def principal():
    opc = 1;
    while(True):
        opc = int(input("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n"));

        if (opc < 1 or opc > 4): break;

        print("\nPrimeiro número:\n");
        num_a = complex(input());
        print("\nSegundo número:\n");
        num_b = complex(input());
        print("\nTerceiro número:\n");
        num_c = complex(input());

        if(opc == 1):
            result = (num_a + num_b + num_c);
            print(result,"Propriedade Real: ", result.real,"Propriedade Imag: ",result.imag)
        elif(opc == 2):
            result = (num_a - num_b - num_c);
            print(result,"Propriedade Real: ", result.real,"Propriedade Imag: ",result.imag)
        elif(opc == 3):
            result = (num_a * num_b * num_c);
            print(result,"Propriedade Real: ", result.real,"Propriedade Imag: ",result.imag)
        elif(opc == 4):
            result = (num_a / num_b / num_c);
            print(result,"Propriedade Real: ", result.real,"Propriedade Imag: ",result.imag)

        print ("\n\n")



principal();