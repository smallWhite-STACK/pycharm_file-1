#@Time : 2021/11/68:36
#@Author : xujian
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
#     请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
#         该函数将返回左旋转两位得到的结果"cdefgab"


# 我的方法与作者的第二个一样
#作者的三个方法：字符串切片 ， 列表遍历拼接 ， 字符串遍历拼接

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s:return
        if n>len(s):
            return s


        li=[]

        for i in range(n,len(s)):
            li.append(s[i])
        for i in range(n):
            li.append(s[i])
        s1="".join(li)
        return s1

if __name__=="__main__":
    s1=Solution()
    print(s1.reverseLeftWords("xujian",5))



