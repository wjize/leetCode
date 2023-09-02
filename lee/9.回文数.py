#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        '''
        python的切片操作,基本语法:
            sequence[start:end:step]
                start: 切片开始的索引（包含在切片中）
                end:   切片结束的索引（不包含在切片中）
                step:  切片步长，用于控制每隔多少个元素取一（如过步长为负数，则从右向左）
        '''
        # 总结
        '''
        列表的每个值有两个索引,正数和负数，如下所示：
        list1   =   [1, 2, 3, 4, 5, 6, 7]
            正数索引  0  1  2  3  4  5  6
            负数索引 -7 -6 -5 -4 -3 -2 -1
        即: list1[0] == list1[-7] 都表示值1
        '''

        # 旧代码
        # if x < 0:
        #     return False
        # return str(x) == str(x)[::-1]

        # 新代码
        # 逻辑: 无变化
        # 优化: 就是简单减少了行数，使用三元表达式解决
        # Feature #9-1 【回文数】 简化代码
        return str(x) == str(x)[::-1] if x >= 0 else False
# @lc code=end

