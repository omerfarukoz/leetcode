class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        svar = str(x)
        r_svar = svar[::-1]
        return svar == r_svar 
