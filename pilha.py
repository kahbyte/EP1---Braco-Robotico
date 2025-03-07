class Pilha:
    def __init__(self, id_pilha):
        self.id = id_pilha  # Identificador da pilha
        self.caixas = []  # Lista de caixas na pilha

    def adicionar_caixa(self, caixa):
        self.caixas.append(caixa)  # Adiciona uma caixa à pilha

    def __repr__(self):
        return f"Pilha {self.id}: {self.caixas}"