#@Time : 2021/11/29:35
#@Author : xujian
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


    #本题的难点在于：python中的字符串无法修改，需要借助list
                    #链表输出为字符串时需要使用下面代码
    #                       ''.join()


# 我的代码： 时间复杂度O（n）  空间复杂度O（n）
class Solution(object):
    def replaceSpace(self, s:str)->str:
        """
        :type s: str
        :rtype: str
        """
        list1=list(s)
        for i in range(len(s)):
            if s[i]==" ":
                list1[i]="%20"
        return ''.join(list1)



    #法2作者：创一个空列表逐次加入成分  （我是修改list的成分）
            # 复杂度分析：
            #
            # # 时间复杂度：遍历使用O(N)，每轮添加（修改）字符操作使用O(1)
            # # 空间复杂度：Python新建的list和Java新建的StringBuilder都使用了线性大小的额外空间
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ':
                res.append("%20")
            else:
                res.append(c)
        return "".join(res)




if __name__=="__main__":
    s=Solution()
    str1="We are happy!"
    print(s.replaceSpace(str1))   #We%20are%20happy!


