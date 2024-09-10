from math import gcd
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current = head
        
        while current and current.next:
            next_node = current.next
            gcd_value = gcd(current.val, next_node.val)
            new_node = ListNode(gcd_value)
            current.next = new_node
            new_node.next = next_node
            current = next_node
        
        return head
