#@Time : 2021/10/3111:09
#@Author : xujian
# 要展示不同数量级的算法，一个好例子就是经典的异序词检测问题。
# 如果一个字符串只是重排了另一个字符串的字符，那么这个字符串就是另一个的异序词，
# 比如 heart 与 earth，以及 python 与 typhon。
    #
    # 为了简化问题，假设要检查的两个字符串长度相同，并且都是由 26 个英文字母的小写形式组成的。
    # 我们的目标是编写一个布尔函数，它接受两个字符串，并能判断它们是否为异序词。

#1.我的想法：
# def check_str(str1,str2):
#     if len(str1)==len(str2):
#         print("ok")
#     else :
#         # return False
#         print("no")
# if __name__=="__main__":
#     str1=repr(input("请输入第一个字符串"))
#     str2=repr(input("请输入第二个字符串"))
#     check_str(str1,str2)


# 方案 1：清点法
        # 清点第 1 个字符串的每个字符，看看它们是否都出现在第 2 个字符串中。
        # 如果是，那么两个字符串必然是异序词。清点是通过用 Python 中的特殊值 None 取代字符来实现的。
        # 但是，因为 Python 中的字符串是不可修改的，所以先要将第 2 个字符串转换成列表。
        # 在字符列表中检查第 1 个字符串中的每个字符，如果找到了，就替换掉。



# 方案 2：排序法

        # 尽管 s1 与 s2 是不同的字符串，但只要由相同的字符构成，它们就是异序词。基于这一点，
        # 可以采用另一个方案。如果按照字母表顺序给字符排序，异序词得到的结果将是同一个字符串。
        # 在 Python 中，可以先将字符串转换为列表，
        # 然后使用内建的 sort 方法对列表排序。

# 方案 4：计数法
#
        # 最后一个方案基于这样一个事实：两个异序词有同样数目的 a、同样数目的 b、同样数目的 c，等等。
        # 要判断两个字符串是否为异序词，先数一下每个字符出现的次数。因为字符可能有 26 种，
        # 所以使用 26 个计数器，对应每个字符。每遇到一个字符，就将对应的计数器加 1。
        # 最后，如果两个计数器列表相同，那么两个字符串肯定是异序词。
def count_num(str1,str2):
    #为每一个str创建个包括26个位置计数器的列表元素
    a1=[0]*26  #代表列表中有26个0
    a2=[0]*26
    #无需将str转换为list
    # list1=list(str1)
    # list2=list(str2)

    i=0
    while i<len(str1):
        num=ord(str1[i])-ord("a")
        a1[num]=a1[num]+1
        i=i+1

    j=0
    while j<len(str2):
        num=ord(str2[j])-ord("a")
        a2[num]=a2[num]+1
        j=j+1

    #此时每一个字母的个数已经出现，我们对比两个列表的对应位置

    #设置一个bool来确定最后答案
    answer=True

    while(i<len(a1)):
        if a1[i]==a2[i]:
            i=i+1
        else :
            answer = False
            print("这两个串不是异序")
            break
    if answer==True:
        print("ok")


if __name__=="__main__":
    str1=input("输出第一个str")
    str2=input("输出第二个str")
    count_num(str1,str2)













