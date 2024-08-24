class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        a, b, c, d = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while a <= b and c <= d:
            for i in range(c, d + 1):
                result.append(matrix[a][i])
            a += 1

            for i in range(a, b + 1):
                result.append(matrix[i][d])
            d -= 1

            if a <= b:
                for i in range(d, c - 1, -1):
                    result.append(matrix[b][i])
                b -= 1

            if c <= d:
                for i in range(b, a - 1, -1):
                    result.append(matrix[i][c])
                c += 1


        return(result)
