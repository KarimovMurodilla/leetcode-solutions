import re

class Solution:
    def remove_star(self, p: str):
        new_p = ''

        for i in p:
            if i == '*' and new_p[-1] == '*':
                continue
            else:
                new_p += i

        return new_p

    def isMatch(self, s: str, p: str) -> bool:
        new_p = self.remove_star(p)
        res = re.match(new_p, s)

        if not res:
            return False
        
        return s == res.group()


s = "aab"
p = "c*a*b"

sol = Solution()
res = sol.isMatch(s, p)
print(res)

