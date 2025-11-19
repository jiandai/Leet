# current version: Runtim 9.56%, Memory 96.15% -> room to improve
class Solution:
    def isPalindromic(self, s: str) -> bool:
        if s is None or len(s)==0:
            return True
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
        return True
    def longestPalindrome(self, s: str) -> str:
        if s is None:
            return None
        if len(s)<=1:
            return s
        keep = []
        for i in range(len(s)-1):
            curr = []
            for j in range(len(s),i,-1):
                print(f"{i}, {j}, {s[i:j]}")
                if self.isPalindromic(s[i:j]):
                    curr = s[i:j]
                    break
            if len(curr) > len(keep):
                keep = curr
        return keep
        
sol = Solution()
print(sol.longestPalindrome("bb"))
