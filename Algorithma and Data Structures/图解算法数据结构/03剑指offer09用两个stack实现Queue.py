#@Time : 2021/11/211:22
#@Author : xujian

# Question:
#     用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
#     分别完成在队列尾部插入整数和在队列头部删除整数的功能。
#     (若队列中没有元素，deleteHead 操作返回 -1 )
from typing import List

class CQueue:

    def __init__(self,s1:List[int],s2:List[int]):
        self.s1=s1
        self.s2=s2

    def appendTail(self, value: int) -> None:
        #判断s2是否为空
        if self.s2==None:
            self.s1.append(value)
        else:
            #现将s2的所有数据搞到s1中才可以
            for i in range(len(self.s2)):
                self.s1.append(self.s2.pop())
            self.s1.append(value)


    def deleteHead(self) -> int:
        #判断s1是否为空
        try:

            if self.s1 == None:
                self.s2.pop()
            elif s1!=None:
                # 现将s1的所有数据搞到s2中才可以
                for i in range(len(self.s1)):
                    self.s2.append(self.s1.pop())
                self.s2.pop()
        except :
            print("-1")
    #
    # def appendTailTwo(self, value: int) -> None:
    #     self.s1.append(value)
    #
    # def deleteHeadTwo(self) -> int:
    #     if self.s2: return self.s2.pop()
    #     if not self.s1: return -1
    #     while self.s1:
    #         self.s2.append(self.s1.pop())
    #     return self.s2.pop()



if __name__=="__main__":
    #s1是用于插入数据
    s1=[1,2,3]
    #s2是用于删除数据
    s2=[]
    cq=CQueue(s1,s2)
    cq.appendTail(9)
    print(s1)
    print("开始删除")
    cq.deleteHead()
    print(s1)
    print(s2)
    cq.deleteHead()
    print(s2)
    cq.deleteHead()
    print(s2)
    cq.deleteHead()
    print(s2)
    #此时已经删完了
    #再删看看会咋样
    cq.deleteHead()




















