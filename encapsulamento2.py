class Aluno:
    def __init__(self, nome, nota=0.0):
        self._nome = nome
        self._nota = float(nota)
    
    @property
    def nome(self):
        """Retorna o nome do aluno."""
        return self._nome
    
    @property
    def nota(self):
        """Retorna a nota do aluno."""
        return self._nota
    
    @nota.setter
    def nota(self, valor):
        """Define a nota do aluno, se estiver entre 0 e 10."""
        if 0 <= valor <= 10:
            self._nota = float(valor)
        else:
            print("Erro: Nota deve estar entre 0 e 10.")
    
    def adicionar_pontos(self, pontos):
        """Adiciona pontos à nota atual, se for positivo."""
        if pontos > 0:
            nova_nota = self._nota + pontos
            self.nota = nova_nota  
            print("Erro: Pontos devem ser positivos.")


if __name__ == "__main__":

    aluno1 = Aluno("João", 7.5)
    print(f"Aluno: {aluno1.nome}")
    print(f"Nota inicial: {aluno1.nota:.1f}")

  
    aluno1.nota = 11.0
    print(f"Nota após tentativa inválida: {aluno1.nota:.1f}")

    aluno1.adicionar_pontos(1.5)
    print(f"Nota após adicionar pontos: {aluno1.nota:.1f}")

    aluno1.adicionar_pontos(-2.0)