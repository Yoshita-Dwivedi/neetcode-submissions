# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle 
        #split & reverse
        #merge

        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        sec = slow.next
        slow.next = None

        temp = sec
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        first = head
        second = prev

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second

            second.next = next_first

            first = next_first
            second = next_second
        



        