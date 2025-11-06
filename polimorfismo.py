class mecanico:
    def consertar(self):
        print("O mecanico está consertando o carro")
        
        class Pessoa:
            def consertar(self):
                print("A pessoa está fingindo ser um mecanico!")
                
            def comer(self):
                print("A pessoa está com a moto quebrada.")
        
        class Gravacao:
            def consertar(self):
                print("som do carro sendo consertado")
        
        class Robo:
            def consertar(self):
                print("som da moto sendo consertado!")
        
        def fazer_conserto(obj):
            obj.consertar()
        
        m = mecanico()
        h = Pessoa()
        g = Gravacao()
        r = Robo()
        
        fazer_conserto(m)
        fazer_conserto(h)
        fazer_conserto(g)
        fazer_conserto(r)
        
        objetos = [mecanico(), Pessoa(), Gravacao(), Robo()]
        for obj in objetos:
            obj.consertar()
