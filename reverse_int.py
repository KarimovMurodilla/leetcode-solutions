class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        reversed_x = str_x[::-1]

        if int(reversed_x) > 2**31:
            return 0
        
        return -int(reversed_x) if x < 0 else int(reversed_x)


x = -899999999915342
s = Solution()
res = s.reverse(x)
print(res)