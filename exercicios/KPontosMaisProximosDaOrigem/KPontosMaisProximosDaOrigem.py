from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Função auxiliar para calcular a distância euclidiana quadrada da origem
        def distance(point):
            x, y = point
            return x * x + y * y

        # Função auxiliar para particionar o array com base na distância da origem
        def partition(left, right):
            pivot = distance(points[right])
            i = left
            for j in range(left, right):
                if distance(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i

        # Função auxiliar para encontrar os k pontos mais próximos usando divisão e conquista
        def find_k_closest(left, right, k):
            if left == right:
                return
            pivot_index = partition(left, right)
            if pivot_index == k:
                return
            elif pivot_index < k:
                find_k_closest(pivot_index + 1, right, k)
            else:
                find_k_closest(left, pivot_index - 1, k)

        find_k_closest(0, len(points) - 1, k)
        return points[:k]

"""
Este código implementa o algoritmo de seleção dos k pontos 
mais próximos da origem no plano XY usando a abordagem de 
divisão e conquista. A função distance calcula a distância 
euclidiana quadrada de um ponto a partir da origem. A função 
partition particiona o array de acordo com as distâncias dos 
pontos e a função find_k_closest utiliza a recursão para 
encontrar os k pontos mais próximos. No final, o código retorna 
os k pontos mais próximos encontrados.
"""