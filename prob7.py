# https://leetcode.com/problems/reverse-integer/description/
class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        elif x<0:
            sign = -1
            x = -x
        else:
            sign = +1
        reversed = 0
        while x>0:
            dig = x % 10
            reversed = reversed*10 + dig
            x = x // 10
        if reversed>=2**31:
            return 0
        return sign * reversed
        
