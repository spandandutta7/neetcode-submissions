# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1, len(lists)):
            lists[i] = self.mergeTwoLists(lists[i - 1], lists[i])

        return lists[-1]

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0, None)
        current = dummy
        # current = list1 if list1 < list2 else current = list2

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return dummy.next
