#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


        '''
        快慢指针

        我们让两个指针 slow 和 fast 分别指向链表头结点 head。
        每当慢指针 slow 前进一步，快指针 fast 就前进两步，这样，当 fast 走到链表末尾时; slow 就指向了链表中点。
        
        如果链表长度为偶数，也就是说中点有两个的时候，我们这个解法返回的节点是靠后的那个节点
        '''
# @lc code=end

