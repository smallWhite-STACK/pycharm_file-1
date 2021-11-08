#@Time : 2021/10/3114:40
#@Author : xujian
#生成列表最快的方式是
#           l = list(range(1000))


#第一个实验就是比较pop()与pop(0)的速度
import timeit
popzero=timeit.Timer("l.pop(0)","from __main__ import l")
popend=timeit.Timer("l.pop()","from __main__ import l")

l=list(range(2000000))
print(popzero.timeit(number=1000))   #1.3812301999999999

l=list(range(2000000))
print(popend.timeit(number=1000))   #5.889999999997286e-05   (小)
#测试1证明pop()就是快，但是证明不了时间复杂度

#第二个实验就是得到许多组数据，比较性能


