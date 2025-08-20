class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        l = 0
        curr = head
        while curr is not None:
            l += 1
            curr = curr.next
        return l
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev, nex = head, None, None
        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ln = self.getLength(head)
        if ln < k:
            return head
        elif ln == k:
            return self.reverseList(head)
        
        # when the length is more than k
        curr = head
        cnt = k-1
        while cnt>0:
            curr = curr.next
            cnt -= 1
        
        rem_list = curr.next
        curr.next = None

        reversed_part = self.reverseList(head)
        crawler = reversed_part

        while crawler.next:
            crawler = crawler.next
        
        crawler.next = self.reverseKGroup(rem_list, k)
        return reversed_part
