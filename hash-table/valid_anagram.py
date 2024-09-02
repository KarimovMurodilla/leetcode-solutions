class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if not d.get(ord(i)):
                d[ord(i)] = 1
            else:
                d[ord(i)] += 1
        
        for i in t:
            if not d.get(ord(i)):
                return False
            d[ord(i)] -= 1

        return sum(d.values()) == 0
            
    
s = "cool😎"
t = "looc😎"

sol = Solution()
res = sol.isAnagram(s, t)

print(res)
