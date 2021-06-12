# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 11:25
# @Author  : Hu-y
# @File    : twoSum.py
# 两数之和
# 需求: 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 核心: num2 = target - num1 是否在nums中

# 解法: ① 暴力解法 ② 排序+双指针  ③ 哈希
from typing import List


class Solution:
    # 1.暴力解法 ==> 双层遍历枚举 nums[i] + nums[j] = target
    # 时间复杂度:O(N^2),其中N是数组中元素的数量。
    # 空间复杂度为: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
        :param nums: input array
        :param target: target value
        Return:
           a list:the index of the nums[i]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 2.排序+双指针 ==>双指针的前提是:有序数组
    # 时间复杂度:O(NlogN)，其中先将数组排序好O(NlogN)，再双指针遍历O(N)得到结果
    # 空间复杂度:O(N)，其中N是数组中的元素数量
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
        :param nums: input array
        :param target: target value
        Return:
            a list:the index of the nums[i]
        """
        # 1. sort
        nums = [[i, v] for i, v in enumerate(nums)]
        print("排序前的数组为:", nums)
        nums = sorted(nums, key=lambda k: k[1], reverse=False)
        print("排序后的数组为:", nums)
        start, end = 0, len(nums) - 1
        # 2. two point
        while start < end:
            temp_sum = nums[start][1] + nums[end][1]
            if temp_sum < target:
                start += 1
            elif temp_sum > target:
                end -= 1
            else:
                return [nums[start][0], nums[end][0]]
        return []

    # 3.哈希 查询target - x 是否在数组中
    # 时间复杂度:O(N)，其中N是数组中的元素数量，对于每一个元素 x，我们可以O(1)地寻找 target - x
    # 空间复杂度:O(N)，其中N是数组中的元素数量。主要为哈希表的开销
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """
        Args:
        :param nums: input array
        :param target: target value
        Return:
            a list:the index of the nums[i]
        """
        hash_res = {}
        for k, v in enumerate(nums):
            if target - v in hash_res:
                print("hash表的结果为:", hash_res)
                return [hash_res[target - v], k]
            hash_res[v] = k
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 15, 20, -5, 7, 11, 15]
    target = 9
    result1 = s.twoSum(nums, target)
    print("暴力解法的结果为:", result1)
    result2 = s.twoSum1(nums, target)
    print("排序+双指针的结果为:", result2)
    result3 = s.twoSum2(nums, target)
    print("hash的结果为:", result3)
