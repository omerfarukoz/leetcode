from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = 0
        n = len(nums)
        flip = 0
        for i in range(n):
            current_value = nums[i] ^ flip
            if current_value == 0:
                a += 1 
                flip ^= 1
            
        return a
