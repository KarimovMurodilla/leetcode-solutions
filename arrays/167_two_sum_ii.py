from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            if sum([numbers[left], numbers[right]]) == target:
                return [left+1, right+1]
            
            elif sum([numbers[left], numbers[right]]) < target:
                left += 1

            else:
                right -= 1

        return []


numbers = [-1,0]
target = -1
s = Solution()
res = s.twoSum(numbers, target)
print(res)
