from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1 = 0
        answer2 = 0

        d_nums1 = {n: 1 for n in nums1}
        d_nums2 = {n: 1 for n in nums2}

        for num1 in nums1:
            if d_nums2.get(num1):
                answer1 += 1

        for num2 in nums2:
            if d_nums1.get(num2):
                answer2 += 1

        return [answer1, answer2]
    

nums1 = [3,4,2,3]
nums2 = [1,5]

s = Solution()
res = s.findIntersectionValues(nums1, nums2)
print(res)
