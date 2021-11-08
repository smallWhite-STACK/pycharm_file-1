#@Time : 2021/11/220:03
#@Author : xujian
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。


#我的思路：建一个列表把链表数据读进去，再利用元组翻转，然后建一个新的链表
class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #空列表
        list_emp=[]
        while(True):
            #此处应该将val装进list中
            # n=head.val
            list_emp.append(1)
            if head!=None:
                head=head.next
            else:
                break
        #翻转list
        list_emp=list_emp[::-1]
        print(list_emp)
        node=self.listToListNode(list_emp)
        return node

    def listToListNode(self,list)->ListNode:
        #因为翻转后第一个为None
        head=ListNode(list[1])
        p=head
        for i in range(2,len(list)):
            p.next=ListNode(list[i])
            p=p.next
        return head




#创建一个ListNode
if __name__=="__main__":
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(3)

    l1.next=l2
    l2.next=l3

    # print(type(s1.reverseList(l1)))   #<class '__main__.ListNode'>
    # print(s1.reverseList(l1))
    print(l1.val)

    s1=Solution()
    s1.reverseList(l1)











