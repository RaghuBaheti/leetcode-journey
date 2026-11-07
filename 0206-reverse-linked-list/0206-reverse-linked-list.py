# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        self.curr = head
        prev = None
        while self.curr is not None:
            nxt = self.curr.next
            self.curr.next = prev
            prev = self.curr
            self.curr = nxt
        return prev