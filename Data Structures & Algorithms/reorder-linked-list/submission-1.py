# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:return
        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        tail = sp
        curr = sp.next
        rev_grp = curr
        prev = None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        rev_grp.next = None
        tail.next = None
        l1 = head
        l2 = prev
        while l2:
            f = l1.next
            s = l2.next
            l1.next = l2
            l2.next = f
            l1 = f
            l2 = s