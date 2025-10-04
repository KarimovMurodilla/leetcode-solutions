

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        sl = ""
        gl = ""
        
        if len(s) != len(goal):
            return False
        if s == goal:
            for i in goal:
                if goal.count(i) > 1:
                    return True
            return False
        for i in range(len(goal)):
            if s[i] != goal[i]:
                sl += s[i]
                gl += goal[i]
            if len(sl) > 2:
                return False
        return sorted(sl) == sorted(gl)


s = "aa"
goal = "aa"
sol = Solution()
res = sol.buddyStrings(s, goal)
print(res)
