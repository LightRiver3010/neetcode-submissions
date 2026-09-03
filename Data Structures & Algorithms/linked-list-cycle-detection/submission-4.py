# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        L = head
        R = head
        while True:
            if R == None or R.next == None:
                return False
            R = R.next
            if R.next == L or R == L:
                return True
            R = R.next
            L = L.next