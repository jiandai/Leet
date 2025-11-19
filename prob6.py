# version 1: Pure math calculation
# Runtime 5.01%, Memory 5.04% :(

class Solution:
    def map1to2(self, i: int, l: int) -> (int, int):
        turn = i // l
        j = i % l
        return turn, j
    def convert(self, s: str, numRows: int) -> str:
        L = len(s)
        if L<=numRows or numRows==1:
            return s
        l = numRows - 1
        if L%l==0:
            T = L//l
            L_arg = L
        else:
            T = L//l +1
            L_arg = L + l - L%l
        K = T // 2
        Parity = T % 2
        if Parity==1:
            C = K*l + 1
        else:
            C = K*l
        print(f"L={L}, l={l}, L_arg={L_arg}, T={T}, K={K}, Parity={Parity}, C={C}")
        Z = [[" "]*C for _ in range(numRows)]
        print(Z)
        for i in range(L):
            turn, j = self.map1to2(i, l)
            k = turn // 2
            parity = turn % 2
            if parity == 0:
                row = j
                col = k * l

            else:
                row = l - j
                col = k *l + j
            Z[row][col] = s[i]
        print(Z)
        output = ""
        for i in range(numRows):
            for j in range(C):
                if Z[i][j] != " ":
                    output += Z[i][j]
        return output

sol = Solution()
#s = "PAYPALISHIRING"
#numRows = 3
s = "ABC"
numRows = 2
print(sol.convert(s, numRows))
