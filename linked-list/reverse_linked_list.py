from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
    
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


node1 = ListNode(5)
node2 = ListNode(4, next=node1)
node3 = ListNode(3, next=node2)
node4 = ListNode(2, next=node3)
head = ListNode(1, next=node4)

s = Solution()
res = s.reverseList(head)

while res:
    print(res.val)
    res = res.next