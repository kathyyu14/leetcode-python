#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        p1 = p2 = dummy

        for i in range(n+1):
            p1 = p1.next
        
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next

        return dummy.next

        '''
        倒数第k个节点获取:
    
        双指针:相隔间距是k, p1 到 k, p2 在 head, 同时前进知道 p1 移动到尾部, 则 p2 可以到达 n - k处

        要删除倒数第 k 个节点, 就得获得倒数第 k + 1 个节点的引用, 则是要获取到 n - k + 1

        dummy节点作用: 防止空指针
        不过注意我们又使用了虚拟头结点的技巧，也是为了防止出现空指针的情况，比如说链表总共有 5 个节点，题目就让你删除倒数第 5 个节点，也就是第一个节点，那按照算法逻辑，应该首先找到倒数第 6 个节点。但第一个节点前面已经没有节点了，这就会出错。

        '''
        
# @lc code=end

