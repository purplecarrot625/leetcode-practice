# Reverse Linked List

初始化:    
current = head  
prev = None  

目标:  

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        return prev
```

# Merge two sorted list
思路:  
造一个假头，一个尾  
两个list遍历，（移动头）谁小加谁，注意最后要拼接上没有走完的l1或者l2  
return dummy head.next
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        l1 = list1
        l2 = list2
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return head.next
```

# 143. Reorder List

首先找到middle    
``` python
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l2 = slow.next
```
然后翻转后半个list    
``` python
   
        # reverse the second list
        prev = slow.next = None
        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
```
最后merge两个list
``` python
# merge two list
        l1, l2 = head, prev
        while l2:
            temp1 = l1.next
            temp2 = l2.next
            
            l1.next = l2
            l2.next = temp1
            
            l1 = temp1
            l2 = temp2
```


# 19. Remove Nth Node From Emd of List

**快慢指针很好用诶**
注意return的是dummy.next  
快慢两个头，很巧的是
``` python
 while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
```
``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next
```

# Copy List with Random Pointer
- 我们要做两次循环，因为有random存在，我们random指向的节点可能还没有被创建
- 用hash结构,新老对应,可以通过curr索引出来copy
``` python
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
        originToCopy = {None:None} # {currentNode: copyNode}
        # map value
        curr = head
        while curr:
            copy = Node(curr.val)
            originToCopy[curr] = copy # map the current node to the copy node
            curr = curr.next #update current pointer
        
        # set pointers
        curr = head
        while curr:
            copy = originToCopy[curr] # the copy of the current node
            # set its pointers
            copy.next = originToCopy[curr.next]
            copy.random = originToCopy[curr.random]
            curr = curr.next
        return originToCopy[head]
```