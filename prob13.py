class Solution:
    def romanToInt(self, s: str) -> int:
        assert s is not None
        if s == "":
            return 0
        num = 0
        # thousand
        if len(s)>=3 and s[:3]=='MMM':
            num = num * 10 + 3
            s = s[3:]
        elif len(s)>=2 and s[:2]=='MM':
            num = num * 10 + 2
            s = s[2:]
        elif len(s)>=1 and s[:1]=='M':
            num = num * 10 + 1
            s = s[1:]
        else:
            num = num * 10 +0
        # hundred
        if len(s) == 0:
            num = num *1000 + 0
            return num
        elif len(s)>=2 and s[:2] =="CM":
            num = num *10 + 9
            s = s[2:]
        elif len(s)>=2 and s[:2] == 'CD':
            num = num * 10 + 4
            s = s[2:]
        elif len(s)>=3 and s[:3] == 'CCC':
            num = num * 10 + 3
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'CC':
            num = num * 10 + 2
            s = s[2:]
        elif len(s)>=1 and s[:1] == 'C':
            num = num * 10 + 1
            s = s[1:]
        elif len(s)>=4 and s[:4] == 'DCCC':
            num = num * 10 + 8
            s = s[4:]
        elif len(s)>=3 and s[:3] == 'DCC':
            num = num * 10 + 7
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'DC':
            num = num * 10 + 6
            s = s[2:]
        elif len(s)>=1 and s[:1] =="D":
            num = num * 10 +5
            s = s[1:]
        else:
            num = num * 10 +0
        # ten
        if len(s) == 0:
            num = num *100 + 0
            return num
        elif len(s)>=2 and s[:2] =="XC":
            num = num *10 + 9
            s = s[2:]
        elif len(s)>=2 and s[:2] == 'XL':
            num = num * 10 + 4
            s = s[2:]
        elif len(s)>=3 and s[:3] == 'XXX':
            num = num * 10 + 3
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'XX':
            num = num * 10 + 2
            s = s[2:]
        elif len(s)>=1 and s[:1] == 'X':
            num = num * 10 + 1
            s = s[1:]
        elif len(s)>=4 and s[:4] == 'LXXX':
            num = num * 10 + 8
            s = s[4:]
        elif len(s)>=3 and s[:3] == 'LXX':
            num = num * 10 + 7
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'LX':
            num = num * 10 + 6
            s = s[2:]
        elif len(s)>=1 and s[:1] =="L":
            num = num * 10 +5
            s = s[1:]
        else:
            num = num * 10 +0
        # one
        if len(s) == 0:
            num = num *10 + 0
            return num
        elif len(s)>=2 and s[:2] =="IX":
            num = num *10 + 9
            s = s[2:]
        elif len(s)>=2 and s[:2] == 'IV':
            num = num * 10 + 4
            s = s[2:]
        elif len(s)>=3 and s[:3] == 'III':
            num = num * 10 + 3
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'II':
            num = num * 10 + 2
            s = s[2:]
        elif len(s)>=1 and s[:1] == 'I':
            num = num * 10 + 1
            s = s[1:]
        elif len(s)>=4 and s[:4] == 'VIII':
            num = num * 10 + 8
            s = s[4:]
        elif len(s)>=3 and s[:3] == 'VII':
            num = num * 10 + 7
            s = s[3:]
        elif len(s)>=2 and s[:2] == 'VI':
            num = num * 10 + 6
            s = s[2:]
        elif len(s)>=1 and s[:1] =="V":
            num = num * 10 +5
            s = s[1:]
        return num

sol = Solution()
#s = "MCMXCIV"
#s= "MDLXX"
#s= "MMCCCVII"
s= "MMMCC"
print(sol.romanToInt(s))
