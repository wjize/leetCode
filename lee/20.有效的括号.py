#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        # Bug #20-1 【有效的括号】当用例为一个字符并且为左括号时，会导致bo无值，return时报错
        # 修改方法，if判断语句修改为 != 这样可减少一次判断，并不会出现问题
        base_bracket = {")":"(", "]":"[", "}":"{"}
        stack = []
        for str in s:
            if str == "(" or str == "[" or str == "{":
                stack.append(str)
            if str == ")" or str == "]" or str == "}":
                if stack.pop() == base_bracket[str]:
                    return False
        return True

# @lc code=end

