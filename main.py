from class_armario import Armario
from class_caixa import Caixa

salas = []
sala = [100, 200, 300, 400, 500, 600,700,800]
for s in sala:
    for x in range (5):
        salas.append(s)
        s += 1


#############
armario = Armario(salas)
caixa = Caixa(601)
armario.adicionar_caixa(caixa)
armario.imprimir()