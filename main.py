from pilha import Pilha
from caixa import Caixa

class Configuracao:
    def __init__(self, num_bases, tamanho_max_pilhas=None, pilha=None, posicao_braco=None):
        self.num_bases = num_bases
        self.tamanho_max_pilhas = tamanho_max_pilhas
        self.pilhas = pilha
        self.posicao_braco = posicao_braco

        def __repr__(self):
            return f"Configuracao(num_bases={self.num_bases}, tamanho_max_pilhas={self.tamanho_max_pilhas}, pilhas={self.pilhas}, posicao_braco={self.posicao_braco})"

def ler_entrada(nome_arquivo):
    pilhas = []
    posicao_braco = []

    with open(nome_arquivo, 'r') as f:
        num_bases = int(f.readline().strip())
        tamanho_max_pilhas = int(f.readline().strip())

        #ler o numero de bases
        for i in range(num_bases):
            pilhas.append(Pilha(i))

        #adicionando as caixas
        for i in enumerate(f):
            for i, linha in enumerate(f):
                valores = linha.strip().split()
                if len(valores) == 1 and valores[0] == 'B':
                    posicao_braco = i
                else:
                    for peso in valores:
                        peso = int(peso)
                        if peso > 0:
                            pilhas[i].adicionar_caixa(Caixa(peso))
        
        return Configuracao(num_bases, tamanho_max_pilhas, pilhas, posicao_braco)
            
def main(): 
    input = ler_entrada('input.txt')
    print(f"Configuração: num bases: {input.num_bases}")
    print(f"tamanho maximo das filas = {input.tamanho_max_pilhas}") 
    for pilha in input.pilhas:
        print(pilha)
    print(f"posicao braço: {input.posicao_braco}")

if __name__ == "__main__":
    main()