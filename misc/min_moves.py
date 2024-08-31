"""
Algorithm:

1. Find intersection
2. Remove from both lists
3. Sort both lists
4. Decrease elements of two sorted lists


12-2 = 10
12-7=5
17-15=3
19-19=0
20-19=1
"""


from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        total = 0
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        
        for i, k in zip(sorted_seats, sorted_students):
            total += abs(i-k)

        return total

s = Solution()

seats = [12,14,19,19,12]
students = [19,2,17,20,7]
res = s.minMovesToSeat(seats, students)
print(res)
