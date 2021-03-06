# 算法必备之N数之和

| 题目       | 两数之和                   | 三数之和                             | 四数之和                                      |
| ---------- | -------------------------- | ------------------------------------ | --------------------------------------------- |
| 解法       | 暴力求解/哈希/排序+双指针  | 排序+双指针                          | 排序+双指针                                   |
| 核心要点   | nums[i] + nums[j] = target | nums[k] + nums[i] + nums[j] = target | ums[k] + nums[m] + nums[i] + nums[j] = target |
| 时间复杂度 | O(N^2)/O(N)/O(NlogN)       | O(N^2)                               | O(N^3)                                        |
| 空间复杂度 | O(1)/O(N)/O(N)             | O(N)                                 | O(N)                                          |

**注:**

- **双指针的前提:有序数组**

- **临界条件的判断**

  

