# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    tmp = ListNode() # initiate
    current = tmp
    carry = 0
    
    # get values from the lists and carryover
    while l1 or l2 or carry:
        if l1:
            i1 = l1.val
            l1 = l1.next # move on
        else: 
            i1 = 0
        if l2:
            i2 = l2.val
            l2 = l2.next # move on
        else:
            i2 = 0
        total = i1 + i2 + carry
        carry = total // 10 # floor

        value = total % 10 # onyly extract the last value
        current.next = ListNode(value)
        current = current.next

    return(tmp.next) # return next because the first is just a 0



    


# add definition to turn list into listnodes
def list_to_linked(x):
    head = ListNode(x[0]) # initiate the linked list with the first element
    current = head
    for num in x[1:]: # define the next values in the linkedlist
        current.next = ListNode(num)
        current = current.next # move along
    return head

l1 = list_to_linked([2,4,3])
l2 = list_to_linked([5,6,4])

result = addTwoNumbers(l1,l2)

