#@Time : 2021/11/414:30
#@Author : xujian
    # 1.
    #     请实现 copyRandomList 函数，复制一个复杂链表。
    #     在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
    #     还有一个 random 指针指向链表中的任意节点或者 null。


    #我的思路是每次复制一个遍历
        #但是不足的地方就是需要在循环外面对复制的新链表头结点单独处理


class Node:
    def __init__(self, x, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        #需要两个变量临时存储next与random
        h1=Node(head)
        zhi=head.val
        tem = head.next
        emp = head.random
        h1.val=zhi
        h1.next=tem
        h1.random=emp
        head=tem
        while(head):
            ls=Node(head)
            ls.val=head.val
            ls.next=head.next
            ls.random=head.random
            head=head.next
        return h1

if __name__=="__main__":
    s1=Solution()
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n1.next=n2
    n2.next=n3
    n1.random=n1
    n2.random=None
    n3.random=n1

    copyhead=s1.copyRandomList(n1)
    print(copyhead.random.val)
    head2=copyhead.next
    head3=head2.next
    print(head3.random.val)




