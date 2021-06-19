# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 21:52
# @Author  : Hu-y
# @File    : 8_mergeArray.py
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Args:
        :param nums1:
        :param m:
        :param nums2:
        :param n:
        :return: None
        """
        # 1 直接合并排序 时间复杂度：O((m+n)log(m+n)) 空间复杂度:O(log(m+n)
        nums1[m:] = nums2
        nums1.sort()

        # 2. 双指针/从前往后 时间复杂度：O(m+n) 空间复杂度:O(m+n)
        # 每次将两个数组中较小的元素放入数组

        sorted = []
        p1, p2 = 0, 0
        while p1 < m or p2 < n:
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted

        # 3. 双指针/从后往前 时间复杂度：O(m+n) 空间复杂度:O(1)
        # 每次将两个数组中较大的元素放入数组1的尾部
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)
