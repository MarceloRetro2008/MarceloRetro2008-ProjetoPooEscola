class pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf

    def apresentar(self) -> str:
        return f"Meu nome é {self.nome}"

class aluno(pessoa):
    def __init__(self, nome: str, cpf: str, matricula: int = None) -> None:
        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matrícula {self.matricula}"

class professor(aluno):
    def __init__(self, nome: str = None, cpf: str = None, matricula: int = None, disciplina: str = None):
        if nome is None:
            nome = input("Digite o nome do professor: ")
        if cpf is None:
            cpf = input("Digite o CPF do professor: ")
        if matricula is None:
            matricula = input("Digite a matrícula do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina do professor: ")
            
        super().__init__(nome, cpf, int(matricula))
        self.disciplina = disciplina
        
    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base}, sou professor de {self.disciplina}"
