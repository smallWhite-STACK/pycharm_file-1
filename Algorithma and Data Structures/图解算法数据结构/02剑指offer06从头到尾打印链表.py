#@Time : 2021/11/29:51
#@Author : xujian

# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）


# 遇到的问题：①list内置的方法reverse()的返回值为None
#                 原因：其实，lista.reverse() 这一步操作的返回值是一个None，
#                 其作用的结果，需要返回调用此方法的list本身就可以了
#
#             ②reversed()的使用
#                 reversed()是python自带的一个方法，准确说，应该是一个类
#

#     字符串，元组，list都可以使用reversed()方法
#         方式:
#             list(reversed(list对象))
#             touble(reversed(元组对象))
#             ''.join(reversed(字符串对象))


#     ①与②详见：https://blog.csdn.net/gymaisyl/article/details/83785853
#


# 我先自己写一个ListNode
class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None

from typing import List
class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        #先使用while循环得到链表的所有元素--》到一个新的list
        i=1  #i代表链表长度
        list1=[]
        while(i):
            list1.append(head.val)
            head=head.next
            if head.next==None:
                list1.append(head.val)
                #法一：
                #使用下一行代码就返回None
                # return list1.reverse()
                #正确的代码--->使用完reverse()后返回原来调用此方法的列表本身
                list1.reverse()
                return list1

                #法二
                #不是使用reverse()而是使用list的函数方法list(reversed(list名字))
                # return list(reversed(list1))
            i = i + 1


    def reversePrintTwo(self, head: ListNode) -> List[int]:

        # return self.reversePrint(head.next) + [head.val] if head else []

        #下面四句等于上面一句
        if head:
            return self.reversePrint(head.next) + [head.val]
        else :
            return []

    def reversePrintThree(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]





if __name__=="__main__":
    l1=ListNode("a")
    l2=ListNode("b")
    l3=ListNode("c")
    l4=ListNode("d")
    l1.next=l2
    l2.next=l3
    l3.next=l4
    print(l1.val)
    print(l2)
    print(l3)
    print(l4)
    print('*'*10)
    s1=Solution()
    # print(s1.reversePrint(l1))   #['d', 'c', 'b', 'a']
    print(s1.reversePrintTwo(l1))  #['d', 'c', 'b', 'a']

























