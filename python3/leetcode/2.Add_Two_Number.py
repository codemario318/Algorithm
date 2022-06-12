# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        curNode = root
        add = 0
        
        while l1 and l2:
            a, b = l1.val, l2.val
            total = a + b + add
            add, res = divmod(total, 10)
            
            curNode.next = ListNode(res);
            curNode = curNode.next
            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            a = l1.val
            total = a + add
            add, res = divmod(total, 10)
            
            curNode.next = ListNode(res);
            curNode = curNode.next
            
            l1 = l1.next
            
        while l2:
            b = l2.val
            total = b + add
            add, res = divmod(total, 10)
            
            curNode.next = ListNode(res);
            curNode = curNode.next
            
            l2 = l2.next
            
        if add > 0:
            curNode.next = ListNode(add)
            
        return root.next