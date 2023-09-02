#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        # Bug #20-1 【有效的括号】当用例为一个字符并且为左括号时return时报错
        # 原因：当用例为一个字符并且为左括号时，会导致bo无值
        # 修改方法，if判断语句修改为 != 这样可减少一次判断，并不会出现问题
        
        # Bug #20-2 【有效的括号】用例为"()"时，无法通过
        # 原因：审题有误，传入的参数是一个字符串而非列表。自己做测试时也是使用list传参，所以未发现
        # 修改方法：重构代码
        base_bracket = {")":"(", "]":"[", "}":"{"}
        stack = []
        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if stack.pop() != base_bracket[s[i]]:
                    # bo = True
                # else:
                    return False
        # return bo
        return True

# @lc code=end

