#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        
        return False


        '''
        快慢指针解决问题

        fast 最终将遇见空指针，说明没有环
        如果 fast and slow 相遇，那肯定是 fast 超过了 slow 一圈后相遇了，说明有环
        '''
# @lc code=end

