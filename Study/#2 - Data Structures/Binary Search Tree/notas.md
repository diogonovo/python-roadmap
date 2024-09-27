Util em operações de busca, inserção e remoção.
Muito usado em Data Science
Cada nó tem apenas dois nós-filho, o da esquerda é menor e o da direita é maior.
(Como os indexes de sql)
Nas arvores de decisão a estrutura da arvore é usada para decidir como classificar a arvore ou prever dados. pode ser uma estrutura subjacente para manipular essas decisões.
Estrutura de indices, uma arvore binaria de buscar para acelerar arecuperação de dados como e Sistemas de Gestão de Banco de Dados.

busca:
Se o valor for igual ao valor do nó atual, o nó foi encontrado.
Se o valor for menor, a busca continua na subárvore à esquerda.
Se o valor for maior, a busca continua na subárvore à direita.

Inserção:
A inserção segue a mesma lógica da busca: começando na raiz, o valor a ser inserido é comparado com os nós até que um local vazio (sem filhos) seja encontrado. O novo valor é então adicionado como uma folha da árvore.

A remoção é mais complexa, pois há três casos principais a considerar:
Remover um nó sem filhos: Apenas remove-se o nó.
Remover um nó com um filho: Substitui-se o nó removido pelo seu único filho.
Remover um nó com dois filhos: Encontra-se o menor valor na subárvore à direita (ou o maior valor na subárvore à esquerda), substitui-se o valor do nó a ser removido por esse valor e remove-se o nó substituto.

Um percurso In-Order numa BST visitará os nós em ordem crescente. Isso é útil para recuperar todos os elementos de uma árvore ordenada.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Inserir um novo nó na BST
def insert(root, key):
    # Se a árvore estiver vazia, retorna um novo nó
    if root is None:
        return Node(key)

    # Caso contrário, recorre para baixo da árvore
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

# Busca na BST
def search(root, key):
    # Base: root é nulo ou a chave está presente na raiz
    if root is None or root.val == key:
        return root

    # O valor da chave é maior que o valor da raiz
    if key > root.val:
        return search(root.right, key)

    # O valor da chave é menor que o valor da raiz
    return search(root.left, key)


Arvores AVL e Arvores Red-Black e Random Forests


AVL Trees vs. Red-Black Trees

AVL Trees:

Principais vantagens:
Altamente balanceadas, o que significa que a complexidade de busca é sempre garantida como O(log n), tornando-as extremamente rápidas para operações de busca em dados ordenados.
Excelente para aplicações onde a busca eficiente é mais importante do que a frequência de inserção ou remoção.

Desvantagens:
Inserções e remoções podem ser mais lentas em comparação com Red-Black Trees devido ao número de rotações necessárias para manter a árvore estritamente balanceada.
Não tão eficientes em cenários onde há muitas inserções e remoções, pois o balanceamento rigoroso adiciona complexidade.

Red-Black Trees:

Principais vantagens:
Flexibilidade: Balanceia a árvore, mas de forma menos rigorosa que uma AVL, resultando em menos rotações e, portanto, inserções e remoções mais rápidas do que em uma AVL.
Muito usadas em sistemas de bancos de dados e em bibliotecas de programação como estrutura de dados padrão (como em dicionários e conjuntos no Java ou C++), pois as operações de inserção e remoção são mais eficientes em cenários com grande volume de dados dinâmicos.

Desvantagens:
A árvore não é tão rigorosamente balanceada quanto uma AVL, então em alguns casos raros a busca pode ser um pouco mais lenta.
Um pouco mais difícil de implementar do que árvores AVL, mas isso é geralmente ocultado por bibliotecas prontas.


Conclusão:

AVL Trees são mais eficientes para busca constante e leitura intensiva. Se estás a trabalhar com dados que mudam raramente, mas precisas fazer buscas rápidas, as árvores AVL são mais apropriadas.
Red-Black Trees são mais eficientes para inserções e remoções frequentes, sendo amplamente usadas em sistemas de alto desempenho que requerem um bom equilíbrio entre operações de busca, inserção e remoção, como em bancos de dados e SGBDs (Sistemas de Gestão de Banco de Dados).

A Random Forest vai usar varias arvores*