#@Time : 2021/11/519:42
#@Author : xujian


class Node():
    def __init__(self,x,next:'Node'=None,random:'Node'=None):
        self.x=x
        self.next=next
        self.random=random

class CopyNode():
    def copycomplexList(self,head:Node):
        dic={}
        #创建一个字典实现将key进行copy得到values
            #注意向字典中加键值对，直接  ：   字典名[key]=value
        #在这将head保留住，下面循环还能用
        mp=head
        while(mp):
            dic[mp]=Node(mp.x)
            mp=mp.next
            #遍历字典修改next与random
        mp2=head
        while(mp2):
            #等号右侧不要用索引，用get方法
            dic[mp2].next=dic.get(mp2.next)
            dic[mp2].random=dic.get(mp2.random)
            mp2=mp2.next
        #返回新链表的head节点
        return dic[head]


#下面的想法是错误的（因为val,next，random都没有处理）


    # def copycomplexListTwo(self,head:Node)->Node:
    #     #拼接加拆分(在原来链表的基础上打断每一个连接，加进去一个复制品)
    #     mp=head
    #     while(mp):
    #         tmp=mp.next
    #         mp=mp.next
    #         mp.next=tmp
    #         mp=tmp
    #     #将包含复制的链表打断
    #     print(head.next.val)


    def copycomplexListTwo(self,head:Node)->Node:
        #拼接加拆分(在原来链表的基础上打断每一个连接，加进去一个复制品)

        #先判断一下是不是空链表
        if not head:
            return

        mp=head
        while(mp):
            #保存下一节点
            tmp=mp.next
            n1=Node(mp.x)
            mp.next=n1
            n1.next=tmp
            mp=tmp
        #注意：random不能在上面的while循环中，因为你复制的应该指向复制的（即a的复制应该指向a的random的复制）
            #而上面一个while没有结束之前，整个链表不完整
        mp=head
        while(mp):
            if mp.random:
                mp.next.random=mp.random.next
            mp=mp.next.next
        #拆分链表
        # mp=head
        # copyHead=head.next
        # while(mp):
        #     tmp=mp.next
        #     mp.next=mp.next.next
        #     tmp.next=tmp.next.next
        #     mp=mp.next
        # return copyHead
        cur = res = head.next
        pre = head
        # 循环终止条件应该是复制链表的next為判断条件
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点
        return res






if __name__=="__main__":
    n1=Node(2)
    n2=Node(3)
    n3=Node(4)
    n1.next=n2
    n2.next=n3
    n3.next=None
    n1.random=n1
    n2.random=None
    n3.random=n2

    cn=CopyNode()
    # head_dic=cn.copycomplexList(n1)
    # print(head_dic.x)

    cc=cn.copycomplexListTwo(n1)
    print(cc.x)






