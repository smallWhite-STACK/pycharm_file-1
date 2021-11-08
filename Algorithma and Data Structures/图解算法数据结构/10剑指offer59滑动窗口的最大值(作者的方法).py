#@Time : 2021/11/721:09
#@Author : xujian


# 本题难点： 如何在每次窗口滑动后，将 “获取窗口内最大值” 的时间复杂度从 O(k)降低至 O(1)。

# Python 通过 zip(range(), range()) 可实现滑动窗口的左右边界 i, j 同时遍历。
# 时间复杂度 O(n)O(n)O(n) ： 其中 nnn 为数组 numsnumsnums 长度；线性遍历 numsnumsnums 占用 O(n)O(n)O(n) ；每个元素最多仅入队和出队一次，因此单调队列 dequedequedeque 占用 O(2n)O(2n)O(2n) 。
# 空间复杂度 O(k)O(k)O(k) ： 双端队列 dequedequedeque 中最多同时存储 kkk 个元素（即窗口大小）。


import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res

    def maxSlidingWindowTwo(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res

