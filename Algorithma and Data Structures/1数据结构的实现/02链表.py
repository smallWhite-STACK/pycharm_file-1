#@Time : 2021/11/28:39
#@Author : xujian

# 创建一个列表  a(10)-->b(6)-->c(5)-->d(98)
class LikeNode():
    def __init__(self,val):
        self.val=val
        self.next=None

if __name__=="__main__":
    ln=LikeNode(10)
    ln2=LikeNode(6)
    ln3=LikeNode(5)
    ln4=LikeNode(98)

    ln.next=ln2
    ln2.next=ln3
    ln3.next=ln4

    print(ln,ln2,ln3)

    #结果可以看出链表的内存不连续，之间通过next指向
    # 0x000001B807775F28
    # 0x000001B8077917B8
    # 0x000001B807791AC8



