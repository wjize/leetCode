#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ''' 
        enumerate() 是 Python 内置函数之一，
        它用于将一个可迭代对象（如列表、元组、字符串等）转换为一个带有索引的枚举对象。
        每个枚举对象都是一个由索引和对应值组成的元组。
        '''
        
        # 示例
        '''
        代码：
        fruits = ['apple', 'banana', 'cherry', 'date']
        for index, fruit in enumerate(fruits):
            print(f"Index {index} corresponds to {fruit}")
        输出：
        Index 0 corresponds to apple
        Index 1 corresponds to banana
        Index 2 corresponds to cherry
        Index 3 corresponds to date
        '''
        
        # 使用 enumerate 获取索引和值
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    return [i, j]

# @lc code=end

