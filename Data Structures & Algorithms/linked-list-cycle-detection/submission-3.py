# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        L, R = head, head
        while R is not None and R.next != None:
            R = R.next
            if R.next == L:
                return True
            elif R.next == None:
                break
            else:
                L = L.next
                R = R.next
            if R.next == L:
                return True
        return False