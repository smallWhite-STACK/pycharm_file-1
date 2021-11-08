#@Time : 2021/11/28:59
#@Author : xujian
#二叉树---（根的值和左右节点指向）
#自定义一个类
class TreeNode():
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

if __name__=="__main__":
    tree1=TreeNode(10)
    tree2=TreeNode(9)
    tree3=TreeNode(8)
    tree4=TreeNode(7)
    tree5=TreeNode(6)

    tree1.left=tree2
    tree1.right=tree3
    tree2.left=tree4
    tree2.right=tree5
















