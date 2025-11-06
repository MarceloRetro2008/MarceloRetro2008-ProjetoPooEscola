from abc import ABC, abstractmethod
from typing import List
from datetime import datetime

# ============================================================================
# POLIMORFISMO EM PYTHON - SUPERCLASSE COM NESTED CLASSES
# ============================================================================
# Demonstra polimorfismo com herança usando uma superclasse
# Classes aninhadas dentro do método consertar()
# ============================================================================


# SUPERCLASSE BASE - Define a interface comum
class Consertador(ABC):
    """Superclasse abstrata que define o contrato para consertadores"""
    
    @abstractmethod
    def consertar(self) -> None:
        """Método abstrato - cada subclasse implementa sua forma"""
        pass


# ============================================================================
# CLASSE MECANICO - Superclasse principal
# ============================================================================
class Mecanico(Consertador):
    """Mecânico profissional que coordena consertos"""
    
    def __init__(self, nome: str = "Mecânico"):
        """Inicializa um mecânico com nome"""
        self.nome = nome
        self.consertos_realizados = 0
    
    def consertar(self) -> None:
        """Método principal que orquestra todo o processo de conserto"""
        print(f"\n🔧 {self.nome} está consertando o carro")
        self.consertos_realizados += 1
        self._executar_consertos()
    
    def _executar_consertos(self) -> None:
        """Executa o processo completo de conserto com classes aninhadas"""
        
        # ====================================================================
        # CLASSES ANINHADAS - Subclasses definidas dentro do método
        # ====================================================================
        
        class Pessoa(Consertador):
            """Pessoa que tenta consertar (subclasse aninhada)"""
            def __init__(self, nome: str = "Pessoa"):
                self.nome = nome
            
            def consertar(self) -> None:
                print(f"  😅 {self.nome} está fingindo ser um mecânico!")
            
            def comer(self) -> None:
                print(f"  🍔 {self.nome} está comendo enquanto a moto está quebrada.")
        
        
        class Gravacao(Consertador):
            """Gravação de áudio (subclasse aninhada)"""
            def __init__(self, tipo: str = "carro"):
                self.tipo = tipo
            
            def consertar(self) -> None:
                print(f"  🔊 Som do {self.tipo} sendo consertado")
        
        
        class Robo(Consertador):
            """Robô que conserta (subclasse aninhada)"""
            def __init__(self, modelo: str = "RX-100"):
                self.modelo = modelo
            
            def consertar(self) -> None:
                print(f"  🤖 Robô {self.modelo} iniciando procedimento de conserto...")
        
        
        # ====================================================================
        # FUNÇÃO POLIMÓRFICA - Aceita qualquer Consertador
        # ====================================================================
        def fazer_conserto(obj: Consertador) -> None:
            """Função que chama consertar() polimorficamente"""
            obj.consertar()
        
        
        # ====================================================================
        # TESTE 1: Chamando fazer_conserto com cada objeto
        # ====================================================================
        print("\n  📌 TESTE 1: Chamando fazer_conserto() com cada objeto")
        print("  " + "-" * 60)
        
        m = Mecanico("João")
        h = Pessoa("Maria")
        g = Gravacao("carro")
        r = Robo("T-800")
        
        fazer_conserto(m)
        fazer_conserto(h)
        fazer_conserto(g)
        fazer_conserto(r)
        
        
        # ====================================================================
        # TESTE 2: Iterando sobre lista de objetos (Polimorfismo!)
        # ====================================================================
        print("\n  📌 TESTE 2: Iterando sobre lista de objetos")
        print("  " + "-" * 60)
        
        objetos = [Mecanico("Pedro"), Pessoa("Ana"), Gravacao("moto"), Robo("RX-200")]
        
        for i, obj in enumerate(objetos, 1):
            print(f"\n  [{i}] Executando conserto...")
            obj.consertar()





# ============================================================================
# DEMONSTRAÇÃO - POLIMORFISMO COM SUPERCLASSE E NESTED CLASSES
# ============================================================================
if __name__ == "__main__":
    print("=" * 70)
    print("🎯 DEMONSTRAÇÃO DE POLIMORFISMO COM SUPERCLASSE")
    print("=" * 70)
    
    # Criando instância do mecânico que orquestra todo o processo
    mecanico_principal = Mecanico("Carlos Silva")
    
    print("\n📌 Iniciando processo de conserto...")
    print("=" * 70)
    
    # Chamando consertar() que executa toda a orquestração
    mecanico_principal.consertar()
    
    print("\n" + "=" * 70)
    print("✅ DEMONSTRAÇÃO CONCLUÍDA!")
    print("=" * 70)
    print("\n💡 CONCEITOS DEMONSTRADOS:")
    print("   ✓ Superclasse abstrata (Consertador)")
    print("   ✓ Herança (Mecanico, Pessoa, Gravacao, Robo herdam de Consertador)")
    print("   ✓ Polimorfismo (cada classe implementa consertar() diferente)")
    print("   ✓ Nested Classes (classes aninhadas dentro do método)")
    print("   ✓ Duck Typing (função fazer_conserto aceita qualquer Consertador)")
    print("=" * 70)

