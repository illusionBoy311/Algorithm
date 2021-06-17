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
        # 遍历
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == '__main__':
    str1 = "()[]{}"
    s = Solution()
    res = s.isValid(str1)
    print(res)
