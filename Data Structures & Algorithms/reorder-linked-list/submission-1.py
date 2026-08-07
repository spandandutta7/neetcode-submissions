# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        stack = []
        node = head
        counter = 0

        while node:
            stack.append(node)
            counter += 1
            node = node.next
        
        current = head
        for _ in range((counter//2)):
            prevNext = current.next
            newNode = stack.pop()
            current.next = newNode
            newNode.next = prevNext
            current = prevNext
        
        current.next = None