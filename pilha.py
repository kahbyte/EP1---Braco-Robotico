class Pilha:
    def __init__(self, id_pilha):
        self.id = id_pilha  # Identificador da pilha
        self.caixas = []  # Lista de caixas na pilha
        self.posicao = None  # Posição da pilha (caso seja o braço mecânico)

    def adicionar_caixa(self, caixa):
        self.caixas.append(caixa)  # Adiciona uma caixa à pilha

    def __repr__(self):
        if self.posicao == 'B':
            return f"Pilha {self.id} (Braço Mecânico)"
        return f"Pilha {self.id}: {self.caixas}"