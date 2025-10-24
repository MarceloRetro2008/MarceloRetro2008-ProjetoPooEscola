class Jogo:
    def __init__(self, titulo=None, genero=None, plataforma=None, preco=None):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        self.preco = preco
        self.avaliacao = None
    
    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Gênero: {self.genero}")
        print(f"Plataforma: {self.plataforma}")
        print(f"Preço: R$ {self.preco:.2f}" if self.preco is not None else "Preço: Não informado")
        print(f"Avaliação: {self.avaliacao if self.avaliacao is not None else 'Não avaliado'}")
    
    def avaliar(self, nota: int):
        if 0 <= nota <= 10:
            self.avaliacao = nota
        else:
            print("A nota deve estar entre 0 e 10")


class JogoTabuleiro(Jogo):
    def __init__(self, titulo=None, genero=None, preco=None, qtd_jogadores=None, pecas=None):
        super().__init__(titulo, genero, "Tabuleiro", preco)
        self.qtd_jogadores = qtd_jogadores
        self.pecas = pecas or []
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Jogadores: {self.qtd_jogadores if self.qtd_jogadores else 'Não especificado'}")
        print(f"Peças: {', '.join(self.pecas) if self.pecas else 'Não especificadas'}")


class JogoRetro(Jogo):
    def __init__(self, titulo=None, genero=None, preco=None, ano_lancamento=None, estado_conservacao=None, midia_original=None):
        super().__init__(titulo, genero, "Retrô", preco)
        self.ano_lancamento = ano_lancamento
        self.estado_conservacao = estado_conservacao or "Bom"
        self.midia_original = midia_original or "Cartucho"
        self.raridade = self.calcular_raridade()
    
    def calcular_raridade(self):
        if not self.ano_lancamento:
            return "Desconhecida"
        idade = 2025 - self.ano_lancamento
        if idade > 30:
            return "Muito Raro"
        elif idade > 20:
            return "Raro"
        return "Comum"
    
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Ano de Lançamento: {self.ano_lancamento}")
        print(f"Estado de Conservação: {self.estado_conservacao}")
        print(f"Mídia Original: {self.midia_original}")
        print(f"Raridade: {self.raridade}")
class JogoEletronico(Jogo):
    
    def __init__(self, titulo=None, genero=None, plataforma=None, preco=None, controlador=None, online=False):
        super().__init__(titulo, genero, plataforma, preco)
        self.controlador = controlador
        self.online = online
        def exibir_informacoes(self):
         super().exibir_informacoes()
        print(f"Controlador: {self.controlador if self.controlador else 'Não especificado'}")
        print(f"Online: {'Sim' if self.online else 'Não'}")
        
if __name__ == "__main__":
    print("=== Jogos Eletrônicos ===")
    jogo1 = JogoEletronico(
        titulo="Final Fantasy VII Remake",
        genero="Aventura, RPG",
        plataforma="PlayStation 4",
        preco=199.90,
        controlador="controle",
        online=True
    )
    jogo1.avaliar(9)
    jogo1.exibir_informacoes()
    
# Exemplo de uso
if __name__ == "__main__":
    print("=== Jogos de Tabuleiro ===")
    jogo_tabuleiro = JogoTabuleiro(
        titulo="War",
        genero="Estratégia",
        preco=149.90,
        qtd_jogadores="2-6",
        pecas=["Tabuleiro", "Dados", "Exércitos"]
    )
    jogo_tabuleiro.avaliar(8)
    jogo_tabuleiro.exibir_informacoes()
    
    print("\n=== Jogos Retrô ===")
    jogo_retro = JogoRetro(
        titulo="Super Mario World",
        genero="Plataforma",
        preco=299.90,
        ano_lancamento=1990,
        estado_conservacao="Excelente",
        midia_original="Cartucho SNES"
    )
    jogo_retro.avaliar(10)
    jogo_retro.exibir_informacoes()
    
    # Adicionando mais um jogo retrô
    print("\n=== Outro Jogo Retrô ===")
    outro_retro = JogoRetro(
        titulo="Altered beast",
        genero="Plataforma",
        preco=60.90,
        ano_lancamento=1990
    )
    outro_retro.exibir_informacoes()