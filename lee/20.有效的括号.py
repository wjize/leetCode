#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        base_bracket = {")":"(", "]":"[", "}":"{"}
        stack = []
        for str in s:
            if str == "(" or str == "[" or str == "{":
                stack.append(str)
            if str == ")" or str == "]" or str == "}":
                if stack.pop() == base_bracket[str]:
                    bo = True
                else:
                    return False
        return bo

# @lc code=end

