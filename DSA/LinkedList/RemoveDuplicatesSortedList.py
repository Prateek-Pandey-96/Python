class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        res = ListNode(-1)
        ptr = res
        
        while head and head.next:
            if head.val != head.next.val:
                res.next = ListNode(head.val)
                res = res.next
            head = head.next
        
        res.next = ListNode(head.val)

        return ptr.next
