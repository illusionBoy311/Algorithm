# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 12:32
# @Author  : Hu-y
# @File    : threeSum.py
# 三数之和
# 需求:给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 思路:排序+双指针(前提:有序数组)
# 核心:nums[i]+nums[j]+nums[k] = target(target=0) 临界条件:① len(nums) < 3判断和 ② 三元组不重复判断
# 排序+迭代1次+双指针
# 时间复杂度：O(N^2)，排序O(NlogN) + 查询比较O(N^2)
# 空间复杂度：O(N)，其中N是数组中的元素数量
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Args:
        :param nums: input array
        Return:
          a list such as [[a,b,c],[a1,b1,c1]]
        """
        # 1.临界条件的判断
        if len(nums) < 3:
            return []
        # 2. sort
        nums = sorted(nums, reverse=False)
        # 3. 去重 ==> 通过set去重
        res = set()
        for i, v in enumerate(nums[:-2]):
            # 剪枝优化
            if v > 0:
                break
            start, end = i + 1, len(nums) - 1
            while start < end:
                if v + nums[start] + nums[end] > 0:
                    end -= 1
                elif v + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    temp = (v, nums[start], nums[end])
                    res.add((temp[0], temp[1], temp[2]))
                    start += 1
        return list(res)


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = s.threeSum(nums)
    print("result=", result)
