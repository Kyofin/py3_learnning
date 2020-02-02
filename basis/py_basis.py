# -*- coding: utf-8 -*-
'''
python3语法学习
'''
import sys  # 要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
reload(sys)
sys.setdefaultencoding('utf-8')

# 循环
the_count = [1,2,3,4,5,6]
for number in the_count:
    if number>3:
        pass
    else:
        print(number)

# 列表生成式
print ("变量为0的一共有:{0}".format(sum([c==0 for c in [0,0,0,1,2,3,45]])))
print ("变量等于A的列表:{0}".format([c for c in ['A','B','C'] if c =='A']))

# （）小括号代表元组
t1 = (13,"13 years old")
print t1

# [] 中括号代表可变序列
l1 = [1,2,3]
l1.append(4)
print l1

# {} 花括号代表字典
m = {"name":"peter","age":18}
print m