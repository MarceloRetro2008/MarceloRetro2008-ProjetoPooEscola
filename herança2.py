class professor(pessoa,aluno):
    def __init__(self, nome=None, matricula=None, disciplina=None):
        if nome is None:
            nome = input("Digite o nome do professor: ")
        if matricula is None:
            matricula = input("Digite a matricula do professor: ")
        if disciplina is None:
            disciplina = input("Digite a disciplina do professor: ")
        super().__init__(nome, matricula)
        self.disciplina = disciplina
        
        def apresentar(self):
            base = super().apresentar()
            return f"meu nome é {self.nome}, minha matricula é {self.matricula}, minha disciplina é {self.disciplina}"
 