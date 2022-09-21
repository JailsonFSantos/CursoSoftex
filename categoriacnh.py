print("Qual a carteira de habilitacao ideal para voce?\n")

rodas = int(input("Quantas rodas tem o Veiculo?\n"))
peso = float(input("Quantos kilos pesa o Veiculo?\n"))
pessoas = int(input("Quantas pessoas cabem no Veiculo?\n"))


if rodas <= 3:
    print("Voce precisa de habilitacao de Categoria 'A'!!")
elif rodas == 4 and pessoas <= 8 and peso <= 3500:
    print("Voce precisa de habilitacao de Categoria 'B'!!")
elif rodas >= 4 and pessoas > 8:
    print("Voce precisa de habilitacao de Categoria 'D'!!")
elif rodas >= 4 and peso > 6000:
    print("Voce precisa de habilitacao de Categoria 'E'!!")
elif rodas >= 4 and peso > 3500 and peso <= 6000:
    print("Voce precisa de habilitacao de Categoria 'C'!!")
else:
    print("Erro")

