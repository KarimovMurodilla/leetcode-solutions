from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0

        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                arr.pop()
                i += 1
            i += 1



arr = [1,2,3]

s = Solution()
res = s.duplicateZeros(arr)
print(res)


"""

[1,0,  2,3,0,  4,5,0]
[1,0,0,2,3,0,0,4]

"""
