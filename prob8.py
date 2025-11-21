# runtime <46.15%, memory <48.86%
class Solution:
    def myAtoi(self, s: str) -> int:
        # what if x=="+" or "-"
        assert s is not None
        if len(s)==0:
            return 0
        result = 0
        sign = +1
        leading_space = True
        check_sign = True
        check_digit = False
        for i in range(len(s)):
            #print(s[i])
            if leading_space:
                if s[i]==" ":
                    continue
                else:
                    leading_space = False
            if check_sign:
                if s[i] == "-":
                    sign = -1                    
                    check_sign=False
                    check_digit = True
                    continue
                elif s[i]=="+":
                    sign = +1
                    check_sign=False
                    check_digit = True
                    continue
                check_sign=False
                check_digit = True
            if check_digit:
                #print(f"-> {s[i]}")
                if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
                    result = result * 10 + int(s[i])
                else:
                    check_digit = False
                    break
        if sign==1 and result >=2**31-1:
            result = 2**31-1
        elif sign==-1 and result >=2**31:
            result = 2**31
        return sign * result

sol = Solution()
#s= "   -042"
#s= "42"
s= "   +0 123"
print(sol.myAtoi(s))
