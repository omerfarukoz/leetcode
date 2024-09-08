class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        perm = [0] * n
        total_xor = 0
        
        for i in range(1, n + 1):
            total_xor ^= i
        
        xor_encoded = 0
        for i in range(1, n - 1, 2):
            xor_encoded ^= encoded[i]
        
        perm[0] = total_xor ^ xor_encoded
        
        for i in range(1, n):
            perm[i] = perm[i - 1] ^ encoded[i - 1]
        
        return perm
