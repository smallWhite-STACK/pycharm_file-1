#@Time : 2021/11/68:54
#@Author : xujian
# 字符串切片
# 字符串遍历拼接
class Solution:

#第一种 : 遇见这种断开字符串的应该想到切片
    def reverseLeftWordsFirst(self,s:str,n:int)->str:
        s1=s[n:len(s):1]
        s1=s1+s[0:n:1]
        return s1

#第三种：效率低下，每轮循环都要新建一个字符串

    #测试时间最长
    # 字符串是 “不可变对象” 。因此，每轮遍历拼接字符时，
    # 都需要新建一个字符串；因此，系统 需申请 NNN 次内存 ，数据量较大时效率低下。

    def reverseLeftWordsThree(self, s: str, n: int) -> str:
        res = ""
        for i in range(n, len(s)):
            res += s[i]
        for i in range(n):
            res += s[i]
        return res

s1=Solution()
print(s1.reverseLeftWordsFirst("xujian",4))

