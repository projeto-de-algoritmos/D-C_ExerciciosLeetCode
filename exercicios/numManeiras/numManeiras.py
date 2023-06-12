from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        def count_ways(arr):
            if len(arr) <= 2:
                return 1
        
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            
            left_count = count_ways(left)
            right_count = count_ways(right)
            
            # Calcula o número de maneiras combinando as contagens
            ways = (left_count * right_count) % MOD
            
            # Calcula o número de permutações usando a fórmula combinatorial
            total_count = self.calculate_combinations(len(left) + len(right), len(left))
            
            # Multiplica o total de contagem pelo número de maneiras
            ways = (ways * total_count) % MOD
            
            return ways
        
        return count_ways(nums) - 1
    
    def calculate_combinations(self, n, k):
        numerator = 1
        denominator = 1
        
        for i in range(k):
            numerator *= (n - i)
            denominator *= (i + 1)
        
        return numerator // denominator