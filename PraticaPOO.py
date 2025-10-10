class console:
   def __init__(self, game=None, marca=None, geração=None, AnoDeLançamento=None, nota=None):
        self.game = game
        self.marca = marca
        self.geração = geração
        self.AnoDeLançamento = AnoDeLançamento
        self.nota = nota
   def descrever(self):
        self.game = input("qual é o seu jogo do seu console favorito? ")
        self.marca = input("qual a marca do seu console? ")
        self.geração = input("qual geração é o seu console? ")
        self.AnoDeLançamento = input("qual o ano de lançamento do seu console? ")
        self.nota = input("qual é a nota do seu console? ")
    
        return f"Esse é o seu {self.game}, favorito e a marca é {self.marca} uma das maiores do mercado, e o seu console é {self.geração} geração, o ano de lançamento do console é de{self.AnoDeLançamento}, é a sua nota final é de {self.nota}"
cs = console()
print(cs.descrever())