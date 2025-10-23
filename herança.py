class pessoa:
    def__init__(self, nome: str) -> None:
    self.nome = nome
    def apresentar(self) -> str: return f"ola eu sou {self.nome}"
class aluno(pessoa):
    def__init__(self, nome: str, matricula: int) -> None:
    super().__init__(nome)
    self.matricula = matricula
    def apresentar(self) -> str:
    base = super().apresentar()
    return f"{base}e sou aluno, matricula {self.matricula}"
class professor(pessoa):
    def__init__(self, nome: str, disciplina: str ) -> None:
    super().__init__(nome)
    self.disciplina = disciplina
    def apresentar(self) -> str:
    base = super().apresentar()
    return f"professor {self.nome} de {self.disciplina}"
class BolsaMixin:
    def calcular_bolsa(self) -> float:
    return 1200

class AlunoBolsista(aluno, BolsaMixin):
   def apresentar(self) -> str:
   base = super().apresentar()
   return f"{base} recebo bolsa de {self.calcular_bolsa():.2f}"
def apresentar_todos(pessoas: list[pessoa]) -> list[str]:
    return [p.apresentar() for p in pessoas]
def main() -> None:
    p = Pessoa("joão")
    a = Aluno("maria", "12345")
    pr = Professor("pedro", "matemática")
    ab = AlunoBolsista("Beatriz", "8456")
    resultados = apresentar_todos([p, a, pr, ab])
    for r in resultados:
        print(r)
    print("",
          f"isinstance(ab, Pessoa): {isinstance(ab, Pessoa)}",
          f"isinstance(ab, Aluno): {isinstance(ab, Aluno)}",
          f"isinstance(ab, BolsaMixin): {isinstance(ab, BolsaMixin)}"
          sep="\n")
   print("MRO de AlunoBolsista:")
   for c in AlunoBolsista.__mro__:
      print("-", cls.__name)
if __name__ == "__main__":
   main()

  