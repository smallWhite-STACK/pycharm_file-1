#@Time : 2021/11/28:45
#@Author : xujian
#Stack栈 --》需要list和ListNode一起实现
        #先进后出

stack=[]
#进栈
stack.append(10)
stack.append('xu')
stack.append(20)
stack.append('jian')

#出栈
stack.pop()
print(stack)   #print(stack)

stack.pop()
print(stack)  #[10, 'xu']

stack.pop()
print(stack)  #[10]

stack.pop()
print(stack)  #[]



