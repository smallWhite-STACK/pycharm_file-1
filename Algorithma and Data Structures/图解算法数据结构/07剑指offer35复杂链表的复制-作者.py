#@Time : 2021/11/415:30
#@Author : xujian
class Node:
    def __init__(self, x, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


# 1.借助Hash表--》字典

#2.拼接+拆分
# 考虑构建 原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> …… 的拼接链表，
#       如此便可在访问原节点的 random 指向节点的同时找到新对应新节点的 random 指向节点。



# 1.
# 时间复杂度 O(N) ： 两轮遍历链表，使用 O(N) 时间。
# 空间复杂度 O(N) ： 哈希表 dic 使用线性大小的额外空间


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]

class SolutionTwo:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        cur = head
        # 1. 复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None # 单独处理原链表尾节点
        return res      # 返回新链表头节点

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
    s=SolutionTwo()
    headCopy=s.copyRandomList(n1)
    print(headCopy.val)


