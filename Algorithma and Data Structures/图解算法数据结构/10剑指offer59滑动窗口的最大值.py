#@Time : 2021/11/720:27
#@Author : xujian
# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #我的思路是使用队列，先进先出的方式
        # 创建一个列表盛放最大值
        maxList=[]
        #先判断链表长度
        if len(nums)<k:return
         #第一步让队列充满k个元素

        d1=deque()
        # 设置一个max(初始值定为list的第一个值)
        max = nums[0]
        for i in range(k):
            d1.append(nums[i])

        #设置一个方法：求队列最大值
        def countListMaxValue(de:deque)->int:
            #定一个起始最大值
            max=de[0]
            for i in de:
                if max<i:
                    max=i
            return max

        firstValue=countListMaxValue(d1)
        #第一个值
        maxList.append(firstValue)

        #第二步队列走出一个，走进一个的方式
        while k<len(nums):
            d1.popleft()
            d1.append(nums[k])
            maxValue=countListMaxValue(d1)
            maxList.append(maxValue)
            k=k+1
        return maxList

if __name__=="__main__":
    li=[0,1,2,3,4,5]
    li2=[-1,56,0,-8,4,75]
    s1=Solution()
    print(s1.maxSlidingWindow(li,3))
    print("徐健在github中的修改")




















