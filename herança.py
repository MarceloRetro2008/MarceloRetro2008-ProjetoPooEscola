class pessoa:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf
        
    def apresentar(self) -> str:
        return f"ola eu sou {self.nome}, CPF: {self.cpf}"

class aluno(pessoa):
    def __init__(self, nome: str, cpf: str, matricula: int) -> None:
        super().__init__(nome, cpf)
        self.matricula = matricula

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} e sou aluno, matricula {self.matricula}"

class professor(pessoa):
    def __init__(self, nome: str, cpf: str, disciplina: str) -> None:
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"professor {self.nome} de {self.disciplina}"

class BolsaMixin:
    def calcular_bolsa(self) -> float:
        return 1200

class AlunoBolsista(aluno, BolsaMixin):
    def __init__(self, nome: str, cpf: str, matricula: int) -> None:
        super().__init__(nome, cpf, matricula)

    def apresentar(self) -> str:
        base = super().apresentar()
        return f"{base} recebo bolsa de {self.calcular_bolsa():.2f}"

def apresentar_todos(pessoas: list[pessoa]) -> list[str]:
    return [p.apresentar() for p in pessoas]

def main() -> None:
    p = pessoa("joão", "1234")
    a= aluno("maria", "4567", 1001)
    pr = professor("pedro", "9876", "matemática")
    ab = AlunoBolsista("Beatriz", "8456", 1002)
    
    resultados = apresentar_todos([p, a, pr, ab])
    for r in resultados:
        print(r)

    print("",
          f"isinstance(ab, pessoa): {isinstance(ab, pessoa)}",
          f"isinstance(ab, aluno): {isinstance(ab, aluno)}",
          f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}",
          sep="\n")
    
    print("MRO de AlunoBolsista:")
    for c in AlunoBolsista.__mro__:
        print("-", c.__name__)

if __name__ == "__main__":
    main()
