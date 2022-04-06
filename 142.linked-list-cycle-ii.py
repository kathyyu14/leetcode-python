#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        
        if not fast or not fast.next:
            return None
        
        fast = head
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow

        '''
        Floyd's Tortoise and Hare 龟兔赛跑算法

        快慢指针相遇后 再将其中一个放到头部同速度一起走 相遇的时候就是pos

        fast 一定比 slow 多走了 k 步，这多走的 k 步其实就是 fast 指针在环里转圈圈，所以 k 的值就是环长度的「整数倍」。

        只要我们把快慢指针中的任一个重新指向 head 然后两个指针同速前进 k - m 步后一定会相遇，相遇之处就是环的起点了。
        '''
        
        # @lc code=end

