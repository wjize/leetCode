#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        ''' 总结
        列表比较重要的就是val, 和next下一个节点。只要有了头节点,就相当于有了整个链表
        所以要想定义一个链表或者获取一个链表, 最先做的是找头节点,没有就定义头节点
        一般头节点不存储数据,所以大部分链表第一元素为head.next。当然也有例外
        '''
        head = ListNode()
        current = head
        
        # Bug #21-1 【合并两个有序链表】链表中有相同元素时，在对比的最后会少数据
        # 原因：缺少一个步骤，当两个列表其中一个遍历结束后，应该将另一个链表直接加进去。不然就会出现上述最后缺数据的情况。
        # 修改方法：循环前的条件判断放到循环后执行。

        # Feature #21-1 【合并两个有序链表】简化代码
        # 优化：逻辑方面无需太多优化，只需将代码尽可能缩短，提高代码可读性

        while list1 and list2:
            if list1.val <= list2.val:
                # 注意：该写法一定注意等号后的第一个元素，一定是赋值等号前的第一个元素。顺序不可乱
                current.next, list1 = list1, list1.next
                # current.next = list1
                # list1 = list1.next
            else:
                current.next, list2 = list2, list2.next
                # current.next = list2
                # list2 = list2.next        
            current = current.next

        # if list1:
        #     current.next = list1
        # elif list2:
        #     current.next = list2
        current.next = list1 or list2
        return head.next

# @lc code=end

