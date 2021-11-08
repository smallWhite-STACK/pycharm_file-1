#@Time : 2021/10/3116:16
#@Author : xujian

# list与dict关于包含的时间复杂度对比

#知识回顾1.
dict_x={j:None for j in range(10)}
print(dict_x)
# {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

#知识回顾2
# random的方法randrange()是从给定的范围返回随机项


#正文开始
import timeit
import random


    #创建一个列表
for i in range(10000,1000001,20000):

    #random.randrange(%d) in x --》我们的目的就是看包含 in 就是看是否被x包含
    t = timeit.Timer("random.randrange(%d) in x "%i, "from __main__ import random,x")

    x=list(range(i))
    time_a=t.timeit(number=1000)

    x={j:None for j in range(i)}
    time_b=t.timeit(number=1000)

    #第一句是错误写法（应该在一个引号里）
    # print("%d", "%10.3f", "10.3f" % (i, time_a, time_b))
    print("%d, %10.3f, %10.3f" % (i, time_a, time_b))




