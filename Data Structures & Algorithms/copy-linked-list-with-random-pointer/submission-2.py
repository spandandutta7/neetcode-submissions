"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashTable = {None:None}

        current = head
        while current:
            hashTable[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            hashTable[current].next = hashTable[current.next]
            hashTable[current].random = hashTable[current.random]
            current = current.next
        
        return hashTable[head]

