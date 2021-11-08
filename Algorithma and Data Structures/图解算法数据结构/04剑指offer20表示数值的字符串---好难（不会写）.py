#@Time : 2021/11/219:01
#@Author : xujian


#题目：
        # 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        #
        # 数值（按顺序）可以分成以下几个部分：
        #
        #     若干空格
        #     一个 小数 或者 整数
        #     （可选）一个 'e' 或 'E' ，后面跟着一个 整数
        #     若干空格
        #
        # 小数（按顺序）可以分成以下几个部分：
        #
        #     （可选）一个符号字符（'+' 或 '-'）
        #     下述格式之一：
        #         至少一位数字，后面跟着一个点 '.'
        #         至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
        #         一个点 '.' ，后面跟着至少一位数字
        #
        # 整数（按顺序）可以分成以下几个部分：
        #
        #     （可选）一个符号字符（'+' 或 '-'）
        #     至少一位数字
        #



# 判断字符\简单字符串是否为数字、字母、混合体
# str.isdigit(): True if 只包含数字；otherwise False。
#
# str.isalpha()：True if 只包含字母；otherwise False。
#
# str.isalnum()：True if 只包含字母或者数字；otherwise False。

class Solution:
    def isNumber(self, s: str) -> bool:
        #先判断字符串中是否有点（只能有一个或者0个）
        count=0
        for i in range(len(str)):
            if str(i)==".":
                count=count+1
                if count>1:
                    return False

        #开头只有两种情况：数字  或者  +-
        if self.firstNum(str(0)):
            #插入一个变量代表前一个字符是啥
            char=''
            for i in range(1,len(s)):

        elif self.secondNum(str(0)):
            return False





    def firstNum(self,s_first:str)->bool:
        return s_first=="+" or s_first=="-"

    def secondNum(self,s_second:str)->bool:
        return s_second.isdigit()

    def otherNum(self,s_e:str)->bool:
        if s_e=="e" or s_e=="E" :
            return True
















