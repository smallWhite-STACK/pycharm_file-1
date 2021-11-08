#@Time : 2021/11/29:21
#@Author : xujian
# 堆--》基于完全二叉树
#       大顶堆  小顶堆
#出堆是   从小到大   按大小出去的
# python需要用到heapq.heappush与heapq.heappop

from heapq import heappush,heappop
# 初始化小顶堆
heap=[]
#人堆
heappush(heap,1)
heappush(heap,3)
heappush(heap,2)
heappush(heap,5)
heappush(heap,4)
heappush(heap,7)
heappush(heap,6)
heappush(heap,10)

#出堆
heappop(heap)
print(heap)  #[2, 3, 6, 5, 4, 7, 10]

















