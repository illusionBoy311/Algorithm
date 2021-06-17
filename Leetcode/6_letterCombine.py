# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 18:05
# @Author  : Hu-y
# @File    : 6_letterCombine.py
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()


        combination = list()
        combinations = list()
        backtrack(0)
        return combinations


if __name__ == '__main__':
    digits = "23"
    s = Solution()
    result = s.letterCombinations(digits)
    print(digits+"的电话号码字母组合结果为:", result)
