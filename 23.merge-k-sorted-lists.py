#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        newList = head = ListNode(-1)

        for ls in lists:
            while ls:
                heappush(heap, ls.val)
                ls = ls.next
        
        while heap:
            head.next = ListNode(heappop(heap))
            head = head.next

        return newList.next


        '''
        优先队列 priority queue 方式来解决
        heapq 通过最小堆 放入进入二叉堆里面 通过pop出最小构造新的list
        '''
                
# @lc code=end

