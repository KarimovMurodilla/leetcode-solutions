from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i
            
        return -1

s = "leetcode"
sol = Solution()
res = sol.firstUniqChar(s)
print(res)
