import random

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

n = 2126753390
pick = 1702766719


def guess(num: int) -> int:
    print(num, pick)
    if num == pick:
        return 0
    elif num > pick:
        return -1
    elif num < pick:
        return

    return num

class Solution:
    # Linear search O(n)
    def guessNumberLinear(self, n: int):
        for i in range(n+1):
            result = guess(i)

            if result == 0:
                return i

    # Bianary search O(log n)
    def guessNumberBinary(self, n: int) -> int:
        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1


s = Solution()
res = s.guessNumberBinary(n)
print(res)