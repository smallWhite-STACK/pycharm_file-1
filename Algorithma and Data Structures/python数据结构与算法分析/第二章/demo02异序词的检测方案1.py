#@Time : 2021/10/3113:15
#@Author : xujian
# 方案 1：清点法
        # 清点第 1 个字符串的每个字符，看看它们是否都出现在第 2 个字符串中。
        # 如果是，那么两个字符串必然是异序词。清点是通过用 Python 中的特殊值 None 取代字符来实现的。
        # 但是，因为 Python 中的字符串是不可修改的，所以先要将第 2 个字符串转换成列表。
        # 在字符列表中检查第 1 个字符串中的每个字符，如果找到了，就替换掉。

def count_num(str1,str2):
    #由于字符串无法进行修改，所以我们将str2进行转换
    list2=list(str2)
    #首先进行个数判断：
    if len(str1)==len(str2):
        i=0
        while(i<len(str1)):
            j=0
            for j in range(len(list2)):
                if str1[i]==list2[j]:
                    list2[j]=None
                else:
                    continue
            i=i+1
        pandun=False
        for i in range(len(list2)):
            if list2[i] == None:
                pandun=True
            else:
                pandun=False
        if pandun==True:
            print("一样")
        else:
            print("不一样")
    else:
        print("长度不等")

# 1.   def anagramSolution2(s1, s2):
# 2.       alist1 = list(s1)
# 3.       alist2 = list(s2)
# 4.
# 5.       alist1.sort()
# 6.       alist2.sort()
# 7.
# 8.       pos = 0
# 9.       matches = True
# 10.
# 11.      while pos < len(s1) and matches:
# 12.          if alist1[pos] == alist2[pos]:
# 13.              pos = pos + 1
# 14.          else:
# 15.              matches = False
# 16.
# 17.      return matches





if __name__=="__main__":
    str1=input("str1")
    str2=input("str2")
    count_num(str1,str2)