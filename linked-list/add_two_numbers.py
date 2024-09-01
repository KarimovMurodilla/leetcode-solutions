from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = ''
        nums2 = ''

        while l1:
            nums1 += str(l1.val)
            l1 = l1.next

        while l2:
            nums2 += str(l2.val)
            l2 = l2.next

        res = str(int(nums1[::-1]) + int(nums2[::-1]))
        
        for i in res[::-1]:
            new_node = ListNode(i)
            if self.head is None:
                self.head = new_node
            else:
                last_node = self.head
                while last_node.next:
                    last_node = last_node.next
                last_node.next = new_node
        
        return self.head