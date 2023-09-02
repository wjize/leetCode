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
        fruits = ['apple', 'banana', 'cherry', 'date']
        for index, fruit in enumerate(fruits):
            print(f"Index {index} corresponds to {fruit}")
        输出：
        Index 0 corresponds to apple
        Index 1 corresponds to banana
        Index 2 corresponds to cherry
        Index 3 corresponds to date
        '''
        
        # 旧代码
        # for i,num1 in enumerate(nums):
        #     for j,num2 in enumerate(nums):
        #         if ( i != j and num1 + num2 == target):
        #             return [i, j]

        # 新代码
        # 逻辑: for循环取到list中第一个元素，计算与target的差值并存储到complement中。
        #       检查complement是否在字典中，若不在则将num与索引值加入字典中，进行下一次循环，避免重复遍历。
        #       若complement在字典中，则将两个值的索引返回。
        # 优化: 使用的字典是哈希索引，所以检索速度特别快，并且减少了一次for循环，宏观上看时间复杂度从o(n^2)降到o(n)

        # Feature #1-1 【两数之和】简化代码,时间复杂度降至o(n)
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
# @lc code=end

