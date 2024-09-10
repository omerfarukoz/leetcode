class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0
        sign = -1 if x < 0 else 1
        x *= sign
        
        while x != 0:
            digit = x % 10
            x //= 10
            if reversed_num > (2**31 - 1 - digit) // 10:
                return 0
            reversed_num = reversed_num * 10 + digit
        
        reversed_num *= sign
        
        return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0
