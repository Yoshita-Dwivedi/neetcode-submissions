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
        if not head:
            return None
        #step 1 : interweave -- copying the linkedlist in between the original
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
        
        #step 2 : assigning pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        #step 3: unweave -- breaking old links
        curr = head
        new_head = head.next

        while curr:
            new_node = curr.next
            curr.next = new_node.next

            if new_node.next:
                new_node.next = new_node.next.next
            curr = curr.next
        return new_head
        