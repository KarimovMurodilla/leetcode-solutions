"""
Input: PAYPALISHIRING

1 2 3 4 5 6 7 8 9 10 11 12 13 14
P A Y P A L I S H I  R  I  N  G
1 2 3 2 1 2 3 2 1 2  3  2  1  2


Output: PAHNAPLSIIGYIR

P   A   H   N
A P L S I I G
Y   I   R

d = {
    1: 'PAHN',
    2: 'APLSIIG',
    3: 'YIR'
}

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d = {}
        n = 1
        operand = '+'

        for i in s:
            if d.get(n):
                d[n] += i
            else:
                d[n] = i

            if n == numRows:
                operand = '-'

            elif n == 1:
                operand = '+'

            n = n + 1 if operand == '+' else n - 1
        res = "".join([char for char in d.values()])
        
        return res



s = 'PAYPALISHIRING'
numRows = 3

sol = Solution()
res = sol.convert(s, numRows)

print(res)