class Aluno:
   def __init__(self, nome=None, sala=None, ano=None, materiaFAV=None, media=None):
        self.nome = nome
        self.sala = sala
        self.ano = ano
        self.materiaFAV = materiaFAV
        self.media = media
   def descrever(self):
        self.nome = input("qual é o nome da sua escola? ")
        self.sala = input("qual a sua sala? ")
        self.ano = input("qual o seu ano? ")
        self.materiaFAV = input("qual a sua matéria favorita? ")
        self.media = input("qual a sua média? ")
    
        return f"o nome da sua escola é {self.nome}, a sua sala é {self.sala}, seu ano é do {self.ano} ano, sua materia favorita é {self.materiaFAV}, é a sua media final é {self.media}"

aluno = Aluno()
print(aluno.descrever())