from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ctr = 0
        for lst in lists:
            if lst is not None:
                heappush(heap, (lst.val, ctr, lst))
                ctr += 1

        merged_list = ListNode(-1)
        ptr = merged_list
        while heap:
            smallest_val, _, smallest = heappop(heap)
            merged_list.next = ListNode(smallest_val)
            merged_list = merged_list.next
            if smallest.next is not None:
                heappush(heap, (smallest.next.val, ctr, smallest.next))
                ctr += 1

        return ptr.next
