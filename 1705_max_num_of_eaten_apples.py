from heapq import heappush, heappop
from typing import List

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        max_heap = []
        total_apples = 0
        day = 0
        
        while day < len(apples) or max_heap:
            if day < len(apples) and apples[day] > 0:
                heappush(max_heap, (day + days[day], apples[day]))
            
            while max_heap and max_heap[0][0] <= day:
                heappop(max_heap)
            
            if max_heap:
                total_apples += 1
                max_heap[0] = (max_heap[0][0], max_heap[0][1] - 1)
                if max_heap[0][1] == 0:
                    heappop(max_heap)
            
            day += 1
        
        return total_apples
