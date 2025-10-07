from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answers = [float("inf")] * n   # изначально все расстояния бесконечность

        # --- 1. Проход слева направо ---
        prev_c = -float("inf")         # "крайне левое" положение символа
        for i in range(n):
            if s[i] == c:
                prev_c = i
            answers[i] = i - prev_c    # расстояние до ближайшего c слева

        print("Проход слева направо:", answers)

        # --- 2. Проход справа налево ---
        next_c = float("inf")          # "крайне правое" положение символа
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                next_c = i
            answers[i] = min(answers[i], next_c - i)  # берём минимум из двух сторон

        print("Проход справа налево:", answers)

        return answers


s = "loveleetcode"
c = "e"
sol = Solution()
res = sol.shortestToChar(s, c)
print(res)


"""
Проход слева направо: [inf, inf, inf, 0, 1, 0, 0, 1, 2, 3, 4, 0]
Проход справа налево: [3,   2,   1,   0, 1, 0, 0, 4, 3, 2, 1, 0]
answers:              [3,   2,   1,   0, 1, 0, 0, 1, 2, 2, 1, 0]
"""
