class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head):
        # Caso base: lista vazia
        if not head:
            return None

        # Caso base: lista contém apenas um elemento
        if not head.next:
            return TreeNode(head.val)

        # Encontra o ponto médio da lista usando o algoritmo do ponteiro rápido e lento
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Divide a lista em duas metades
        prev.next = None

        # Cria o nó da árvore com o valor do ponto médio
        node = TreeNode(slow.val)

        # Chama recursivamente a função para construir as subárvores esquerda e direita
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)

        return node
    
"""
Este código implementa a conversão de uma lista 
ordenada em uma árvore de busca binária. A função 
sortedListToBST recebe o head da lista como entrada. 
O algoritmo utiliza a técnica do ponteiro rápido e 
lento para encontrar o ponto médio da lista, dividindo-a 
em duas metades. Em seguida, é criado um nó da árvore com 
o valor do ponto médio. A função é chamada recursivamente 
para construir as subárvores esquerda e direita, e o nó é 
retornado como raiz da árvore resultante.
"""