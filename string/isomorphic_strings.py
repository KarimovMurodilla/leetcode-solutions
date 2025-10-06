class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if t[i] in d.values() and not d.get(s[i]):
                return False

            if d.get(s[i]) and d.get(s[i]) != t[i]:
                return False

            else:
                d[s[i]] = t[i]
            d[s[i]] = t[i]
        
        return True
    

s = "paper"
t = "title"

sol = Solution()
res = sol.isIsomorphic(s, t)
print(res)
