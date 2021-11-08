#@Time : 2021/11/28:51
#@Author : xujian
#Queue先进先出
#   python需要借助外包

#       关于collections  --》  https://www.cnblogs.com/dianel/p/10787693.html

from collections import deque

#错误写法调用deque()
# d1=deque[]

#进队
d1=deque()
d1.append(10)
d1.append(123)
d1.append('xujian')

#出队
d1.popleft()
print(d1)
d1.popleft()
print(d1)
d1.popleft()
print(d1)

# deque([123, 'xujian'])
# deque(['xujian'])
# deque([])






