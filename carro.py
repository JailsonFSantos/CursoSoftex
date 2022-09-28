class Carro():
 def __init__(self, cor, marca, modelo, ano, km_rodados):
   self.cor = cor
   self.marca = marca
   self.modelo = modelo
   self.ano = ano
   self.km_rodados = km_rodados


    

car_1 = Carro("azul", "Fiat", "Palio", 2005, 185000)

car_2 = Carro("Branco", "Ford", "Ka", 2010, 60000)

car_3 = Carro("Amarelo", "Chevrolet", "Onix", 2010, 58200)

print(car_1.modelo, car_1.cor)

print(car_2.marca,car_2.cor)

print(car_3.modelo,car_3.km_rodados)
   