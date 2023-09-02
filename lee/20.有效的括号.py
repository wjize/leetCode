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

        # Bug #20-3 【有效的括号】当用例为"((("时返回ture,与预期不符，应为false
        # 原因：如果都为左括号，则不会进入到比较的分支中，也不会输出false。
        # 修改方法：如果所有括号都匹配，则最后的stack中不应该有任何元素，退出for循环后，再次进行判断输出

        # Bug #20-4 【有效的括号】当用例为"){"时，程序出异常
        # 原因：如果第一个字符是右括号，此时stack中不会有数据，stack.pop()则会出现返回空的错误
        # 修改方法：增加条件判断,因为如果第一个字符为右括号，那他一定是不匹配的

        # Bug #20-5 【有效的括号】当用例为"()"时，返回结果为false，与预期不符
        # 原因：if stack.pop() != base_bracket[s[i]] or len(stack) == 0:该步条件判断先pop，后判断
        # 修改方法：将长度判断先比较，就不会出问题了。
        base_bracket = {")":"(", "]":"[", "}":"{"}
        stack = []
        if len(s) == 1 or s[0] in [")", "]", "}"]:
            return False
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            if s[i] in [")", "]", "}"]:
                if len(stack) == 0 or stack.pop() != base_bracket[s[i]]:
                    # bo = True
                # else:
                    return False
        # return bo
        # return True
        # if len(stack) == 0:
        #     return True
        # else:
        #     return False
        return len(stack) == 0

# @lc code=end

