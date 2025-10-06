class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Time: O(logn) - Log base 26 of n
        res = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res += chr(ord('A') + offset)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]


s = Solution()
result = s.convertToTitle(2147483647)
print(result)
