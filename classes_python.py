class Bicicleta:

    def  __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim, Plim")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")
    
    def correr(self):
        print("vrummmmmm")


b1 = Bicicleta("vermelha","Caloi", 2022, 189)

b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)