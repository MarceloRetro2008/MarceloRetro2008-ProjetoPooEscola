class Moto:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h!")
    def frear(self, valor):
        self.velocidade -= valor
        if self.velocidade < 0:
            self.velocidade = 0
            print(f"{self.modelo} reduziu para {self.velocidade} km/h.")
    def detalhes(self):
        return (f"{self.marca} {self.modelo} ({self.ano}) - " f"Cor: {self.cor}, Velocidade: {self.velocidade} km/h")

moto1 = Moto("Honda", "CBR", 2022, "vermelho")
moto2 = Moto("yamaha", "mt-07", 2021, "azul")

print(moto1.detalhes())
print(moto2.detalhes())
moto1.acelerar(90)
moto2.acelerar(50)
moto1.frear(20)
moto2.frear(15)
print(moto1.detalhes())
print(moto2.detalhes())

if moto1.velocidade > moto2.velocidade:
    print(f"{moto1.modelo} está mais rápido que {moto2.modelo}")
elif moto1.velocidade < moto2.velocidade:
    print(f"{moto2.modelo} está mais rápido que {moto1.modelo}")
else:
    print("ambos os motos estão com a mesma velocidade")