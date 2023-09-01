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
        st = ""

        # 【Bug #2】 当测试用例为["flower","flower","flower","flower"]时，返回结果为"flow"。预期应为"flower"
        # 原因：for循环遍历是以列表最大长度为准，用例本应该判断6次，却因为列表最大长度为4.导致缺少两次步骤。
        # 修改方法：for循环的遍历以列表中最短长度为准
        # for i in range(len(strs)):

        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            s = [char[:i+1] for char in strs]
            if len(set(s)) == 1:
                st = s[0]
            else:
                break
        return st
# @lc code=end