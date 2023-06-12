from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)  # Obtém o tamanho das listas nums1 e nums2
        pairs = 0  # Variável para contar o número de pares que satisfazem as condições
        
        for i in range(n):
            for j in range(i+1, n):
                # Verifica a condição nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
                if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
                    pairs += 1  # Incrementa o contador de pares
        
        return pairs  # Retorna o número de pares que satisfazem as condições