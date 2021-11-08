#@Time : 2021/10/3110:48
#@Author : xujian
#计算前前n个数的和
def sum(n):
    sum_num=n*(n+1)/2
    return sum_num

if __name__=="__main__":
    n=int(input("请输入数字"))
    print(sum(n))




