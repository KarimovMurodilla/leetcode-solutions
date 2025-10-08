class Solution:
    def twoNumberSum(self, array: list, targetSum: int):
        left, right = 0, len(array) - 1

        array.sort()
        print(array)

        while left < right < len(array):
            print(left, right)
            if targetSum == sum([array[left], array[right]]):
                return [array[left], array[right]]
            
            elif targetSum > sum([array[left], array[right]]):
                print(sum([array[left], array[right]]))
                left += 1
            
            else:
                right -= 1

        return []


array = [-21, 301, 12, 4, 65, 56, 210, 356, 9, -47] # [-47, -21, 4, 9, 12, 56, 65, 210, 301, 356]
targetSum = 163
s = Solution()
res = s.twoNumberSum(array, targetSum)
print(res)
