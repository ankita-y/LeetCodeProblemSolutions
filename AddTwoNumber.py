# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = l1[::-1]
        l1 = int(''.join(map(str,l1)))

        l2 = l2[::-1]
        l2 = int(''.join(map(str, l2)))

        l3 = list(map(int,str(l1+l2)))
        print(l3)


s = Solution()
s.addTwoNumbers([2,4,3],[5,6,4])