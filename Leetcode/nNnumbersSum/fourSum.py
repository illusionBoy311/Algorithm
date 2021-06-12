# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 22:50
# @Author  : Hu-y
# @File    : fourSum.py
# 四数之和
# 需求:给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
# 找出所有满足条件且不重复的四元组。注意：答案中不可以包含重复的四元组。
# 思路: 排序+ 双指针

# 排序+迭代2次+双指针
# 核心:nums[i]+nums[j]+nums[k]+nums[m] = target 固定nums[k]和nums[m] ==> 两数之和 与 三数之和的解法
# 时间复杂度:O(N^3)，排序O(NlogN) + 查询比较O(N^3)
# 空间复杂度:O(N)，其中N是数组中的元素数量
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Args:
        :param nums: input array
        :param target:
        Return:
            a list
        """
        # 1. 临界条件的判断
        if len(nums) < 4:
            return []
        # 2. 排序
        nums = sorted(nums, reverse=False)
        # 3. 去重
        res = set()
        # 4.双指针
        for i, i_v in enumerate(nums[:-3]):
            for j, j_v in enumerate(nums[i + 1:-2]):
                start, end = i + j + 2, len(nums) - 1
                while start < end:
                    sum_val = i_v + j_v + nums[start] + nums[end]
                    if sum_val > target:
                        end -= 1
                    elif sum_val < target:
                        start += 1
                    else:
                        temp = [i_v, j_v, nums[start], nums[end]]
                        res.add((temp[0], temp[1], temp[2], temp[3]))
                        start += 1
        return list(res)


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    result = s.fourSum(nums, target)
    print("result=", result)
