while True:
    ent = input("是否继续(y/n):")
    if ent == "n":
        break
    input_string = input("请输入:")
    # strs = input_string.split(',')

    class Solution:
        def isValid(self, s: str) -> bool:
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

    mytest = Solution()
    print(mytest.isValid(input_string))