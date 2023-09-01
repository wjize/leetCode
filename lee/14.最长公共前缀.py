#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 首次编写，本次代码执行用例报错。
        # 原因：用例中可能没有公共前缀，这样就不会走if分支。st也就未定义。在返回时提示st就会出现异常。
        # 修改方法：先初始化st字符串
        st = ""
        for i in range(len(strs)):
            s = [char[:i+1] for char in strs]
            if len(set(s)) == 1:
                st = s[0]
            else:
                break
        return st
# @lc code=end