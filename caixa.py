class Caixa:
    def __init__(self, peso, pilha=None):
        self.peso = peso  # Peso da caixa
        self.pilha = pilha  # Referência à pilha onde a caixa está

    def __repr__(self):
        return f"Caixa({self.peso}kg)"