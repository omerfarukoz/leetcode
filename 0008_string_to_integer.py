class Solution:
    def myAtoi(self, s: str) -> int:
        val = 0
        sign = 1
        digitFound = False
        signFound = False
        for ch in s.lstrip():
            if ch.isdigit():
                digitFound = True
                num = ord(ch) - ord("0")
                val = val * 10 + num
            elif ch in ["-", "+"] and not signFound and not digitFound:
                signFound = True
                if ch == "-":
                    sign = -1
            else: 
                break

        return max(-2**31, min(val * sign, 2**31-1))
