# EP1---Braco-Robotico

EP 1 de Inteligência Artificial feito com base nas seguintes especificações: https://crivelaro.notion.site/Bra-o-Rob-tico-d1b21eea93b346c99d3c03af9bb5024e

# Modelagem do Problema e Conclusões

Esta seção apresenta a modelagem do problema do empilhamento de caixas e a análise dos algoritmos de busca utilizados para solucioná-lo.

---

## 1. Modelagem de Estados e Ações

- **Estados:**  
  Cada estado representa a disposição das caixas nas bases (pilhas) e a posição do braço mecânico, que é identificado por "B".

  - As pilhas são representadas como tuplas de inteiros (pesos das caixas), obedecendo à restrição de limite máximo (por exemplo, 3 ou 4 caixas por pilha).
  - O estado final é definido quando as caixas estão ordenadas (em ordem decrescente de peso) nas posições iniciais, enquanto as demais posições estão vazias (com zeros).

- **Ações:**  
  Uma ação corresponde ao movimento do braço mecânico que consiste em:
  - **Pegar (P):** Retirar a caixa do topo de uma pilha.
  - **Soltar (S):** Colocar a caixa no topo de outra pilha.  
    Cada ação é registrada com a posição de origem, a posição de destino e o valor da caixa movimentada.

---

## 2. Função Sucessora dos Estados e as Ações Possíveis

- **Geração dos Sucessores:**  
  Para cada estado, o algoritmo percorre as posições (exceto a que contém o braço) e identifica as ações válidas:
  - Seleciona a caixa do topo de uma pilha.
  - Verifica se a posição de destino não é a do braço, se a pilha destino não está cheia e se a caixa a ser colocada respeita a ordem de peso (somente pode ser colocada se o valor da caixa no topo da pilha destino for maior).

Cada ação gera um novo estado onde a caixa é removida da origem e adicionada na pilha de destino.

---

## 3. Checagem do Objetivo

- **Verificação do Estado Final:**  
  O estado objetivo é pré-definido e consiste na configuração em que:
  - As primeiras posições (à esquerda) possuem as caixas ordenadas de forma decrescente.
  - A posição do braço permanece inalterada.
  - As demais posições ficam vazias ou são completadas com zeros.
- **Algoritmo de Verificação:**  
  A checagem é realizada comparando cada pilha do estado atual com o estado objetivo. Se todas as pilhas (exceto a do braço) estiverem corretas, o objetivo foi alcançado.

---

## 4. Função Heurística

- **Conceito e Cálculo:**  
  A função heurística estima o custo restante para alcançar o estado final.
  - Para cada caixa, calcula-se a distância (em número de casas) entre sua posição atual e a posição onde ela deve estar.
  - Aplica-se um fator de custo unitário: se a distância for de 1 casa, o custo é 1; para distâncias maiores, utiliza-se um fator (por exemplo, 0.75 por casa).
  - Adiciona-se um custo extra baseado no peso da caixa (cada 10kg acrescenta 1 de energia).

Essa soma dos custos para todas as caixas fornece uma estimativa do “esforço” necessário para atingir o objetivo.

---

## 5. Função Custo

- **Cálculo do Custo de um Movimento:**  
  Cada movimento possui custo composto por:
  - **Custo de deslocamento:**
    - Se o movimento é de 1 casa, o custo é 1 de energia.
    - Movimentos maiores (por exemplo, extensão do braço para 4 casas) possuem um custo menor por casa (por exemplo, 0.75 por casa ou um custo fixo, conforme a implementação).
  - **Custo pelo peso da caixa:**
    - Cada 10kg de peso acrescenta 1 de energia ao custo.

Portanto, o custo total de um movimento é a soma do custo de deslocamento e do acréscimo pelo peso da caixa.

---

## 6. Função A\* (A-estrela)

- **Integração da Heurística com o Custo:**  
  O algoritmo A\* utiliza a soma do custo acumulado (g) e da estimativa heurística (h) para determinar o valor f = g + h de cada nó.
  - **g:** Custo já gasto para alcançar o estado atual.
  - **h:** Estimativa do custo restante (calculada conforme descrito na função heurística).

Essa combinação orienta a busca pelo caminho ótimo, equilibrando o que já foi investido e o que ainda falta para alcançar o objetivo.

---

## 7. Exemplo do Algoritmo e Passos

### Situação Exemplo:

- **Estado Inicial:**

  - Posição 0: [30]
  - Posição 1: [20]
  - Posição 2: B
  - Posição 3: [10, 5]
  - Posição 4: [7, 2, 1]

- **Estado Final (Objetivo):**
  - Posição 0: [30, 20, 10]
  - Posição 1: [7, 5, 2]
  - Posição 2: B
  - Posição 3: [1, 0, 0]
  - Posição 4: [0, 0, 0]

### Caminho e Número de Passos (Exemplo Ilustrativo):

- **Dijkstra:**

  - **Teoria:**  
    Baseia-se apenas no custo acumulado (g) para expandir os nós.
  - **Observação:**  
    Explora um grande número de estados porque não utiliza nenhuma orientação (heurística) para direcionar a busca.
  - **Exemplo:**  
    Pode expandir centenas ou milhares de estados antes de encontrar o caminho ótimo.

- **Ganancioso (Greedy):**

  - **Teoria:**  
    Seleciona os nós com base somente na heurística (h), tentando escolher a direção que aparenta estar mais próxima do objetivo.
  - **Observação:**  
    Geralmente é mais rápido, mas não garante a solução ótima, podendo explorar mais estados se a estimativa não for precisa.
  - **Exemplo:**  
    Pode expandir um número intermediário de estados (ex.: 620 estados) mas com risco de não encontrar o melhor caminho.

- **A\*:**
  - **Teoria:**  
    Equilibra o custo acumulado (g) com a heurística (h) para selecionar o próximo nó a expandir.
  - **Observação:**  
    Tende a explorar menos estados e a encontrar o caminho ótimo, pois utiliza a informação do custo já investido e a estimativa do esforço restante.
  - **Exemplo:**  
    Pode expandir menos estados (ex.: 468 estados) e é considerado o mais indicado para problemas complexos.

---

## 8. Comparação dos Algoritmos

- **Dijkstra:**

  - **Vantagem:** Garante encontrar o caminho ótimo.
  - **Desvantagem:** Pode ser muito ineficiente em espaços de estados grandes, pois não utiliza uma heurística para guiar a busca.

- **Ganancioso (Greedy):**

  - **Vantagem:** Pode ser rápido em determinadas configurações, pois foca em minimizar a distância ao objetivo.
  - **Desvantagem:** Não garante a solução ótima e pode expandir muitos estados se a heurística não for precisa.

- **A\*:**
  - **Vantagem:** Combina o melhor dos dois mundos, encontrando o caminho ótimo de forma eficiente na maioria dos casos.
  - **Desvantagem:** Em situações com heurísticas mal definidas ou estados muito complexos, o desempenho pode diminuir, mas geralmente é o algoritmo ideal para este problema.

A escolha do algoritmo ideal depende da complexidade do estado inicial:

- Em cenários simples ou onde o estado inicial está próximo do objetivo, o Ganancioso pode ser suficiente.
- Em configurações mais complexas, com um espaço de estados grande, o A\* é preferível por balancear custo e estimativa.
- Dijkstra pode ser utilizado como base, mas tende a ser menos eficiente em problemas com muitas possibilidades de movimento.

---

## 9. Apresentação do Modelo na Tela e Caminho Ótimo

- **Representação dos Estados:**  
  Cada estado é impresso mostrando as pilhas e a posição do braço. Por exemplo:
  Posição 0: 30 20 10
  Posição 1: 7 5 2
  Posição 2: B
  Posição 3: 1 0 0
  Posição 4: 0 0 0

- **Movimentos do Braço Mecânico:**  
  A sequência de ações (movimentos) é apresentada com detalhes como:
- **Direção:** "E" (esquerda) ou "D" (direita).
- **Casas Movidas:** Número de casas deslocadas.
- **Ação:** "P" (pegar) ou "S" (soltar).
- **Custo:** Energia gasta no movimento.

O caminho ótimo é aquele que minimiza o custo total (soma dos custos de movimentação e do peso) e é obtido pela sequência de ações gerada pelo algoritmo de busca.

---

## Conclusão

A modelagem apresentada permite:

- Representar o problema de empilhamento de caixas com restrições de ordem e capacidade.
- Gerar estados e movimentos válidos por meio de uma função sucessora.
- Calcular de forma matemática os custos de cada movimento (incluindo deslocamento e peso) e uma estimativa heurística para orientar a busca.

A comparação entre os algoritmos mostra que:

- **Dijkstra** explora muitos estados e pode ser ineficiente.
- **Ganancioso** pode ser rápido, mas sem garantia de solução ótima.
- **A\***, por combinar custo e heurística, é geralmente o mais adequado, especialmente em cenários complexos.

Esta abordagem permite imprimir o estado final e a sequência de movimentos, facilitando a visualização do caminho ótimo encontrado pelo algoritmo.
