#@Time : 2021/10/3113:15
#@Author : xujian
# 方案 2：排序法

        # 尽管 s1 与 s2 是不同的字符串，但只要由相同的字符构成，它们就是异序词。基于这一点，
        # 可以采用另一个方案。如果按照字母表顺序给字符排序，异序词得到的结果将是同一个字符串。
        # 在 Python 中，可以先将字符串转换为列表，
        # 然后使用----list------内建的 sort 方法对列表排序。

def sort_fun(str1,str2):
    # list1=list(str1).sort()
    # list2=list(str2).sort()
        #sort()没有返回值

    list1=list(str1)
    list2=list(str2)
    list1.sort()
    list2.sort()

    #对其进行比较
    panduan=False
    i=0
    while(i<len(list1)):
        if list1[i]==list2[i]:
            i=i+1
            panduan=True
        else:
            panduan=False
            break
    return panduan

if __name__=="__main__":
    str1=input("输出第一个str")
    str2=input("输出第二个str")
    print(sort_fun(str1,str2))
