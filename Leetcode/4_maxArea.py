# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 9:01
# @Author  : Hu-y
# @File    : 4_maxArea.py

# 盛水最多的容器:双指针
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(ans, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return ans

    def maxArea1(self, height: List[int]) -> int:
        maxarea = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
        return maxarea


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    result = s.maxArea(height)
    result1 = s.maxArea(height)
    print("盛水最多的容器面积为:", result)
    print("====================================")
    print("盛水最多的容器面积为:", result1)
