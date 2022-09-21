from datetime import date
current_date = date.today()
data_atual = current_date.year


nome = input("Digite seu nome completo!")
ano_nasc = int(input("Digite o ano de nascimento com 4 digitos!"))
while ( ano_nasc <= 1922  or ano_nasc > 2021 ):
	ano_nasc = int(input("Digite o ano de nascimento com 4 digitos!"))
idade = data_atual - ano_nasc


print(nome,"tem ou tera" ,idade, "anos, no ano de", current_date.year, "!")