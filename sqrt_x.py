class Solution:
    def mySqrt(self, x: int) -> int:
        odd_num = 1
        count = 0
        
        while not x <= 0:
            x -= odd_num
            odd_num += 2
            count += 1

            print(x)

        return count

s = Solution()
res = s.mySqrt(8)
print(res)