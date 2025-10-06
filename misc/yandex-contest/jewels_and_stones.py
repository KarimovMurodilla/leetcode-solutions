class Solution:
    def count_jewels(self, j, s):
        count = 0

        for i in s:
            if i in j:
                count += 1

        return count

j = input()
s = input()

sol = Solution()
res = sol.count_jewels(j, s)
print(res)
