class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxe = mine = result = nums[0]
        for num in nums[1:]:
            if num < 0:
                maxe, mine = mine, maxe
            
            maxe = max(num, num * maxe)
            mine = min(num, num * mine)
            
            result = max(result, maxe)
        
        return result
