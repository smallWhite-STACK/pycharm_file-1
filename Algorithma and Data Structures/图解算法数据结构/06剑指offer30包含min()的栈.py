#@Time : 2021/11/319:11
#@Author : xujian
# 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
#     调用 min、push 及 pop 的时间复杂度都是 O(1)。

        #
        # 普通栈的 push() 和 pop() 函数的复杂度为 O(1) ；而获取栈最小值 min()
        # 函数需要遍历整个栈，复杂度为 O(N) 。
        #
        # 本题难点： 将 min() 函数复杂度降为 O(1) 。


#我的代码：有一个缺陷：
#             当list2中删除元素正好是最小时u，你li3返回的仍然是被删除的那个数
#         （1）我计划的修改MinStackTwo：将li3中存入多个最小值（即li2每输入一个数，只要是其当前最小的，就加到li3中）

        #我的原始代码还是修改的（1）与作者版本的不同是传入的参数不同，用法不同而已


            #重大缺陷是由于传入的是一个list：所以时间复杂度不满足要求O(1)


#作者的代码MinStackThree


class MinStack:

    li2=[]
    li3=[]
    #python我们使用list代替Stack
    def __init__(self,li):
        self.li=li

    def push(self)->None:
        self.li3.append(self.li[0])
        for i in range(len(self.li)):
            self.li2.append(self.li[i])
            if self.li3[0]>self.li[i]:
                self.li3[0]=self.li[i]

    def pop(self)->None:
        self.li2.pop()
    def top(self)->int:
        return self.li2[-1]

    def min(self)->int:
        return self.li3[-1]

class MinStackTwo:

    #下面两句代码其实可以放在__init__函数中
    # li2=[]
    # li3=[]
    #python我们使用list代替Stack
    def __init__(self,li):
        self.li=li
        self.li2,self.li3=[],[]

    def push(self)->None:
        # self.li3.append(self.li[0])   #①
        for i in range(len(self.li)):
            self.li2.append(self.li[i])
            # if self.li3[-1]>self.li[i]:  #②


            #①②可以被下面这句总和都一起
            if not self.li3 or self.li3[-1]>self.li[i]:
                self.li3.append(self.li[i])

    def pop(self)->None:

        if self.li2.pop()==self.li3[-1]:
            self.li3.pop()

    def top(self)->int:
        return self.li2[-1]

    def min(self)->int:
        return self.li3[-1]

class MinStackThree:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]




if __name__=="__main__":
    li=[115,2,-78983,4,56,-456,-45]
    ms=MinStackTwo(li)
    ms.push()
    ms.pop()
    ms.pop()
    print(ms.min())
    print(ms.top())

#作者的和我的只是用法不同
    # mt=MinStackThree()
    # mt.push(10)
    # mt.push(-12)
    # mt.push(-456)
    # mt.push(456)
    # print(mt.top())
    # print(mt.min())








