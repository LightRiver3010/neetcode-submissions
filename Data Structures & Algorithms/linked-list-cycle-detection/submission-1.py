# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        L = head
        R = L
        while True:
            if R.next == L:
                return True
            if R.next == None:
                return False
            R = R.next
            if R.next == L:
                return True
            if R.next == None:
                return False
            R = R.next
            L = L.next