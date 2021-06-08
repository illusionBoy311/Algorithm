# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 22:25
# @Author  : Hu-y
# @File    : 1_longestPalindrome.py
# 思路:对于一个子串而言,如果它是回文,且长度大于2,那么去掉首尾的两个字母之后,它仍然是个回文串。
import string as str


class Solution:
    # 动态规划的状态转移方程 P(i,j)表示字符串s的第i到j字母字母组成的字符串 状态转移方程: P(i,j) = P(i+1,j-1)^(Si==Sj)
    # 即为s[i+1:j-1]是回文串,并且s的第i和j个字母相同时,s[i:j]才会是回文串。
    # 对于长度为1的子串,它显然是个回文串；对于长度为2的子串,只要它的两个字母相同,它就是一个回文串。
    # 边界条件:P(i,i) = true && P(i,i+1) = (Si == Si+1)
    # 结合状态转移方程以及边界条件得到:所有P(i,j)=true中j-i+1的最大值
    # 注意:在状态转移方程中,从长度较短的字符串向长度较长的字符串进行转换,因此一定要注意动态规划的循环顺序
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j]表示s[i..j]是否为回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界,左边界的上限可以设置宽松一些
            for i in range(n):
                # 由L和i可以确定右边界,即j-i+1=L得
                j = L + i - 1
                # 如果右边界越界,即可退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                # 只要dp[i][j] == True成立,即表示子串[i..L]是回文串,此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


if __name__ == "__main__":
    s = Solution()
    str = "cbbd"
    result = s.longestPalindrome(str)
    print(result)

