#删除排序链表中的重复元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        last, cur = head, head.next
        while True:
            while cur and cur.val == last.val:
                cur = cur.next
            last.next = cur
            last = cur
            if not cur: break
            cur = cur.next
        return head
