#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 首次编写，本次代码执行用例报错。
        # 【Bug #1】当测试用例无返回值，代码执行报错
        # 原因：用例中可能没有公共前缀，这样就不会走if分支。st也就未定义。在返回时提示st就会出现异常。
        # 修改方法：先初始化st字符串
        # st = ""

        # 【Bug #2】 当测试用例为["flower","flower","flower","flower"]时，返回结果为"flow"。预期应为"flower"
        # 原因：for循环遍历是以列表最大长度为准，用例本应该判断6次，却因为列表最大长度为4.导致缺少两次步骤。
        # 修改方法：for循环的遍历以列表中最短长度为准
        # for i in range(len(strs)):

        ''' 代码优化
        ' 注意到代码中,在每个迭代步骤中都创建了一个名为 s 的临时列表,这是不必要的。
        ' 可以直接比较字符串数组 strs 中的元素，避免创建额外的列表。
        '''
        # 修改方法：可以只将列表中第一个字符串作为比较标准进行比较比较后直接将字符串拼接
        # 调用all()方法做判断
        '''
        ' all() 是一个内置函数,用于检查可迭代对象中的所有元素是否都为真(True)。它返回一个布尔值：
        ' 如果可迭代对象中的所有元素都为真，则 all() 返回 True。
        ' 如果可迭代对象中的至少一个元素为假(False),或者可迭代对象为空,all() 返回 False。
        '''

        st = ""
        min_len = min(len(s) for s in strs)
        # for i in range(len(strs)):
        for i in range(min_len):
            char = strs[0][i]
            # s = [char[:i+1] for char in strs]
            #if len(set(s)) == 1:
            if all(s[i] == char for s in strs):
                st += char
            else:
                break
        return st
# @lc code=end