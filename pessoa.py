class servivo:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def respirar(self):
        print(f"{self.nome} está respirando...")
        
    def dormir(self):
        print(f"{self.nome} está dormindo...")

class Pessoa(servivo):
    def falar(self, mensagem):
        print(f"{self.nome} diz: {mensagem}.")

    def andar(self, destino):
        print(f"{self.nome} está andando até {destino}.")

    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")

p1 = Pessoa("edilberto", "25")
p2 = Pessoa("maria","26")   
print("=======================================")
p1.respirar()
p1.dormir()
p1.falar("hello")
p1.andar("china")
p1.comer("pizza")

print("=======================================")

p2.respirar()
p2.dormir()
p2.falar("hello bizonho")
p2.andar("japão")
p2.comer("arroz")
print("=======================================")