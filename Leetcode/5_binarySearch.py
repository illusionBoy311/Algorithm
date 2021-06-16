# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 11:38
# @Author  : Hu-y
# @File    : 5_binarySearch.py
# 二分查找:双指针
from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    s = Solution()
    result = s.binarySearch(nums, target)
    print("二分查找的结果为:", result)
