class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a'] * n
        
        for i in range(n):
            max_value_at_i = min(26, k - (n - i - 1))
            result[i] = chr(ord('a') + max_value_at_i - 1)
            k -= max_value_at_i
            
        return ''.join(result[::-1])
