# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 20:35
# @Author  : Hu-y
# @File    : 7_isValid.py
# 有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        # 判断字符串长度
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = list()
        # 遍历字符串
        for ch in s:
            if ch in pairs:  # 如果遇到右括号,需要匹配一个和右括号相同类型的左括号
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)  # 如果遇到左括号,直接入栈
        return not stack


if __name__ == '__main__':
    str1 = ""
    s = Solution()
    res = s.isValid(str1)
    print(res)
