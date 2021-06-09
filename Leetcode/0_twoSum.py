# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 12:40
# @Author  : Hu-y
# @File    : 0_twoSum.py
# 两数之和 关键在于 num2 = target - num1 是否在给定的数组中
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力解法
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        # 优化1 -> 双重for循环编程单层for循环
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - nums[i]
            if num2 in nums:
                if num1 == num2 and nums.count(num2) == 1:
                    continue
                return [i, nums.index(num2, i + 1)]
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # 优化2 -> 对于num2的遍历,仅仅需要遍历num1前后的元素即可
        for i in range(1, len(nums)):
            temp = nums[:1]
            if target - nums[i] in temp:
                return [temp.index(target - nums[i]), i]
        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        # 优化3 -> 使用dict处理
        dict = {}
        for i, n in enumerate(nums):
            if target - n in dict:
                return [dict[target - n], i]
            dict[i] = n
        return []


if __name__ == '__main__':
    nums = [0, 0, 4, 15]
    target = 19
    s = Solution()
    result = s.twoSum(nums, target)
    result1 = s.twoSum1(nums, target)
    result2 = s.twoSum1(nums, target)
    result3 = s.twoSum1(nums, target)
    print(result)
    print(result1)
    print(result2)
    print(result3)
