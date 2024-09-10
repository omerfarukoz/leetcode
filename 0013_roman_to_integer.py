class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        pre_val = 0
    
        for char in s:
            value = romans[char]
            if value > pre_val:
                total += value - 2 * pre_val
            else:
                total += value
            pre_val = value
        
        return total
