#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        '''
        ' 旧版代码，本想将特殊字符优先处理，之后在按正常逻辑处理其他罗马数
        ' 但是审题错误，以为特殊字符只有这六种，不会出现其他的
        ' 实际上 MIV 表示的数是 M:1000 + IV:4 = 1004。旧版代码逻辑则是将其算作 M:1000 + I:1 + V:5 = 1006
        ' 属于基础代码编译问题
        '''
        # special_str = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        # if s in special_str.keys():
        #     return special_str[s]
        # sum = 0
        # base_str = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        # for i in range(len(s)):
        #     sum += base_str[s[i]]
        # return sum

        '''
        ' 修正代码
        ' 优化: 将特殊字符转换成正常算数逻辑字符
        ' 如: 若s = MIV 中有IV, 则先将其替换为IIII, 此时s变化为MIIII。这样就可以用正常逻辑计算值了
        '''
        sum = 0
        base_str = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        s = s.replace("IV","IIII").replace("IX","VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in range(len(s)):
            sum += base_str[s[i]]
        return sum
# @lc code=end

