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

        优先队列 pq 中的元素个数最多是 k 所以一次 push 或者 pop 方法的时间复杂度是 O(logk)
        所有的链表节点都会被加入和弹出 pq 所以算法整体的时间复杂度是 O(Nlogk)，其中 k 是链表的条数 N 是这些链表的节点总数。
        '''
                
# @lc code=end

