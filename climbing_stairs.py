"""
Case 2:
1. 1+1=2
2. 2
- Answer = 2

Case 3:
1. 1+1+1=3
2. 1+2=3
3. 2+1=3
Answer = 3

Case 4:
1. 1+1+1+1=4
2. 1+1+2=4
3. 1+2+1=4
4. 2+1+1=4

5. 2+2=4
Answer = 5

Case 5:
1. 1+1+1+1+1=5
2. 1+1+1+2=5
3. 1+1+2+1=5
4. 1+2+1+1=5
5. 2+1+1+1=5

6. 2+1+2=5
7. 2+2+1=5

8. 1+2+2=5
Answer = 8

Case 6:
1. 1+1+1+1+1+1=6
2. 1+1+1+1+2=6
3. 1+1+1+2+1=6
4. 1+1+2+1+1=6
5. 1+2+1+1+1=6
6. 2+1+1+1+1=6

7. 1+1+2+2=6
8. 1+2+1+2=6
9. 1+2+2+1=6

10. 2+1+1+2=6
11. 2+1+2+1=6
12. 2+2+1+1=6

13. 2+2+2=6
Answer = 13

"""

from itertools import permutations

class Solution:
    def climbStairs(self, n: int) -> int:
        ln = [1] * n
        n = 1

        while ln.count(1) > 1:
            ln.remove(1)
            ln.remove(1)
            ln.append(2)

            comb = set(permutations(ln))
            n += len(comb)
        
        return n


s = Solution()
res = s.climbStairs(8)
print(res)