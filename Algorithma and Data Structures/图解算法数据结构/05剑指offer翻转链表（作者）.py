#@Time : 2021/11/221:20
#@Author : xujian
class ListNode():
    def __init__(self,val):
        self.val=val
        self.next=None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre


if __name__=="__main__":
    l1=ListNode(1)
    l2=ListNode(2)
    l3=ListNode(3)

    l1.next=l2
    l2.next=l3
    s1=Solution()
    print(s1.reverseList(l1).val)






