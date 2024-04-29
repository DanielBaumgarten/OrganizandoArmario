class Caixa:
    def __init__(self, num_sala):
        self.numero = num_sala
        self.chave = None
        self.caneta = None 
        self.ctrl_ar = None
        self.ctrl_projetor = None

    def get_numero(self):
        return self.numero
