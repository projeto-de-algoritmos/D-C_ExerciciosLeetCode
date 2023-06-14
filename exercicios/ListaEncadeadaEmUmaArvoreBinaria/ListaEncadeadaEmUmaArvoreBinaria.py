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