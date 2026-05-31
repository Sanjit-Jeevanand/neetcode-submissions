# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        while True:
            prev_head = curr
            curr = curr.next
            tail = curr
            for _ in range(k):
                if not curr:
                    return dummy.next
                curr = curr.next
            nhead = curr
            prev = None
            curr = prev_head.next
            for _ in range(k):
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn
            prev_head.next = prev
            tail.next = nhead
            curr = tail