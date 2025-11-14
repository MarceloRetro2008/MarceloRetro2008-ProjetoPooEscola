class Animal:
    def __init__(self, nome, especie, cor, tamanho):
        self.nome = nome
        self.especie = especie
        self.cor = cor
        self.tamanho = tamanho
    
    def emitir_som(self):
        return None
    
    def descrever(self):
        return f"""
        Nome: {self.nome}
        Espécie: {self.especie}
        Cor: {self.cor}
        Tamanho: {self.tamanho}
        Som: {self.emitir_som()}
        """

class Reptil(Animal):
    def __init__(self, nome, especie, cor, tamanho):
        super().__init__(nome, especie, cor, tamanho)
    
    def emitir_som(self):
        return "Ssssss (som de réptil)"

class Ave(Animal):
    def __init__(self, nome, especie, cor, tamanho):
        super().__init__(nome, especie, cor, tamanho)
    
    def emitir_som(self):
        return "Piu piu! (canto de pássaro)"

class Peixe(Animal):
    def __init__(self, nome, especie, cor, tamanho):
        super().__init__(nome, especie, cor, tamanho)
    
    def emitir_som(self):
        return "Glub glub! (som de bolhas)"

class Mamifero(Animal):
    def __init__(self, nome, especie, cor, tamanho):
        super().__init__(nome, especie, cor, tamanho)
    
    def emitir_som(self):
        return "Som de mamífero"

if __name__ == "__main__":

    animais = [
        Animal("Animal Genérico", "Animalia", "Marrom", "Médio"),
        Reptil("Cobra", "Réptil", "Verde", "2 metros"),
        Ave("Pardal", "Ave", "Marrom", "Pequeno"),
        Peixe("Dourado", "Peixe", "Laranja", "30 cm"),
        Mamifero("Cachorro", "Canino", "Preto", "Grande")
    ]
    
  
    for animal in animais:
        print(animal.descrever())
        print("-" * 50)
