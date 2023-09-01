#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            s = [char[:i+1] for char in strs]
            if len(set(s)) == 1:
                st = s[0]
            else:
                break
        return st
# @lc code=end