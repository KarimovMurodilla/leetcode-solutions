from collections import Counter


class Solution:
    def greatestLetter(self, s: str) -> str:
        counts = Counter(s)
        max_letter_ord = 0
        answer = ""

        for i in s:
            if i.isupper() and counts.get(i.lower()):
                if ord(i) > max_letter_ord:
                    answer = i
                    max_letter_ord = ord(i)
            elif i.islower() and counts.get(i.upper()):
                if ord(i.upper()) > max_letter_ord:
                    answer = i.upper()
                    max_letter_ord = ord(i.upper())

        return answer


s = "AbCdEfGhIjK"
sol = Solution()
res = sol.greatestLetter(s)
print(res)
