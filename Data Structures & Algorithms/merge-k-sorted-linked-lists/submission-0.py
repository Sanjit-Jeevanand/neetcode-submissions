# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range(len(lists)):
            heapq.heappush(h,(lists[i].val,i))
        dummy = ListNode(0)
        curr = dummy
        while h:
            _,i = heapq.heappop(h)
            curr.next = ListNode(lists[i].val)
            curr = curr.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(h,(lists[i].val,i))
        return dummy.next