class Armario:
    def __init__(self,salas):
        self.prateleira = {}
        for sala in salas:
            self.prateleira[sala] = None #None = prateleira vazia
    
    def adicionar_caixa(self, caixa):
        num_cx = caixa.get_numero()
        self.prateleira[num_cx] = caixa

    def imprimir(self):
        print("Prateleiras: ")
        for prateleira in self.prateleira.items():
            print(prateleira) 