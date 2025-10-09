class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}

        for letter in s:
            if d.get(letter):
                return letter
            d[letter] = 1
    

s = "jkodgypoya"
sol = Solution()
res = sol.repeatedCharacter(s)
print(res)
