# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenIdxNode = head
        oddIdxNode = head.next if head else None

        while evenIdxNode and oddIdxNode:
            evenIdxNode.val, oddIdxNode.val = oddIdxNode.val, evenIdxNode.val
            
            evenIdxNode = oddIdxNode.next
            oddIdxNode = evenIdxNode.next if evenIdxNode else None
            
        return head