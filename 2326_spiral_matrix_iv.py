class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        matrix = [[-1] * n for _ in range(m)]
        
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        index = 0
        
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                if index < len(values):
                    matrix[top][i] = values[index]
                    index += 1
            top += 1
            
            for i in range(top, bottom + 1):
                if index < len(values):
                    matrix[i][right] = values[index]
                    index += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    if index < len(values):
                        matrix[bottom][i] = values[index]
                        index += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    if index < len(values):
                        matrix[i][left] = values[index]
                        index += 1
                left += 1
        
        return matrix
