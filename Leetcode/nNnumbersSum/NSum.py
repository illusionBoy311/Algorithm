# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 23:05
# @Author  : Hu-y
# @File    : NSum.py
# N数之和 排序 + 递归迭代N-1次 + 双指针
from typing import List


class Solution:
    def NSum(self, nums: List[int], n: int, target: int) -> List[List[int]]:
        """
        Args:
        :param nums:
        :param n:
        :param target:
        :return: a list
        """
        # 1. 临界条件判断
        if len(nums) < n:
            return []
        res = []

        if n == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
                return res
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                sub_res = self.NSum(nums[i + 1:], n - 1, target - nums[i])
                for j in range(len(sub_res)):
                    res.append([nums[i]] + sub_res[j])
            return res
