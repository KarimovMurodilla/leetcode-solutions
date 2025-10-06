class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        a = b = 0

        while b < len(typed):
            if a < len(name) and name[a] == typed[b]:
                a += 1
                b += 1

            elif b > 0 and typed[b] == typed[b-1]:
                b += 1

            else:
                return False

        return a == len(name)


name = "alex"
typed = "aaleexeex"

s = Solution()
res = s.isLongPressedName(name, typed)
print(res)



"""
alex
    |


aaleexeex
      |


a = b = 0

while b < len(typed):
    if a < len(name) and name[a] == typed[b]:
        a += 1
        b += 1

    elif b > 0 and typed[b] == typed[b-1]:
        b += 1

    else:
        return False

return a == len(name)

"""
