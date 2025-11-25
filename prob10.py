'''
Leet P10 runtime <18.78%, memory <63.42%
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(f"s={s}, p={p}")
        assert s is not None and p is not None
        if len(s)==0 and len(p)==0:
            return True
        elif len(s)>0 and len(p)==0:
            return False
        elif len(s)==0 and len(p)>0:
            last_ch_p = p[-1]
            if last_ch_p != "*":
                return False
            else: 
                return self.isMatch(s, p[:-2])
        else:
            last_ch_s = s[-1]
            last_ch_p = p[-1]
            if last_ch_s == last_ch_p or last_ch_p=='.':
                return self.isMatch(s[:-1],p[:-1])
            elif last_ch_p=="*":
                if p[-2]!="." and last_ch_s!=p[-2]:
                    return self.isMatch(s,p[:-2])
                else:
                    """
                    Hardest case:
                    add `or self.isMatch(s,p[:-2])` to handle cases like s='a', p='ab*a*' or p='aa*a*a*' etc
                    """
                    return self.isMatch(s[:-1],p) or self.isMatch(s,p[:-2])
            else:
                return False
        
sol = Solution()
#s = 'aab'
#p = 'c*a*b'
#s = "mississippi"
#p = "mis*is*p*."
#s='ab'
#p='.*c'
#s = 'aaa'
#p = 'ab*a'
#s = "a"
#p = "ab*"
#s = "bbbba"
#p = ".*a*a"
#s = "aaa"
#p = "ab*a*c*a"
#s= "a"
#p= "ab*a*"
s= "a"
p= "aa*a*a*"
print(sol.isMatch(s,p))
