"""作用于序列的运算符和函数"""

"""加法运算符"""
# print([1,2,3]+[4,5,6])
# print((1,2,3)+(4,5,6))
# print("123"+"456")

"""乘法运算符"""
# print([1,2,3]*3)
# print((1,2,3)*3)
# print("123"*3)

"""id()函数"""
# s=[1,2,3]
# print(id(s))
# s*=2
# print(id(s))

"""is和is not运算符""" #检测对象的id值是否相等
# print([1,2,3] is [1,2,3]) #列表是可变对象，id值不相等
# print([1,2,3] is not [1,2,3]) #列表是可变对象，id值不相等
# print("123" is "123") #字符串是不可变对象，id值相等
# print((123) is (123)) #不可变对象，id值相等

"""in和not in运算符""" #检测对象是否在序列中
# print(1 in [1,2,3])
# print(1 not in [1,2,3])
# print(1 in (1,2,3))
# print(1 not in (1,2,3))
# print('1' in "123")
# print('1' not in "123")

"""del语句""" #用于删除一个或多个指定的对象
# s=[1,2,3]
# del s[0]
# print(s)

# x="FishC"
# y=[1,2,3]
# del x,y
# print(x) 输出就会报错 NameError: name 'x' is not defined 因为x和y都被删除了
# print(y)

# x=[1,2,3,4,5]
# del x[1:4] #删除1到4的元素 左闭右开
# print(x)

# x=[1,2,3,4,5]
# x[1:4]=[] #将1到4的元素替换为空列表
# print(x)

"""clear()方法""" #清空列表中的所有元素
# x=[1,2,3,4,5]
# x.clear() #清空列表
# print(x)
# """del(清空列表中的所有元素)"""
# x=[1,2,3,4,5]
# del x[:]
# print(x) #删除所有元素

"""序列相关的函数"""

"""列表 元组和字符串相互转换""" # list() tuple() str()
# print(list("FishC"))
# print(list((1,2,3,4,5)))
# print(tuple("FishC"))
# print(tuple([1,2,3,4,5]))
# print(str([1,2,3,4,5]))
# print(str((1,2,3,4,5)))

"""max()和min()函数""" #返回序列中最大值和最小值 
"""传入单个参数"""
# s=[1,1,2,3,5]
# print(max(s))
# t="FishC"
# print(max(t))

#s=[]
# print(max(s)) #报错 ValueError: max() arg is an empty sequence
# print(max(s, default="空列表")) #default参数指定空列表时返回的默认值

"""传入多个参数"""
# print(min(1,1,2,3,5))
# print(max(1,1,2,3,5))

"""len()和sum()函数""" #len()返回序列中元素个数 sum()返回序列中所有元素的和

"""sorted()和list(reversed())函数""" #sorted()返回一个排序后的新序列 reversed()返回一个反转后的新序列
"""sort()和reverse()方法""" #sort()对原序列进行排序 reverse()对原序列进行反转
# s=[1,2,3,0,6,4,5]
# print(sorted(s))  #返回一个排序后的新序列
# print(s) #原序列不变
# s.sort()
# print(s) #原序列已经改变

# t=["FishC","Python","C","Java"]
# print(sorted(t))
# print(sorted(t,key=len))

# s=[1,2,5,8,0]
# print(reversed(s)) #返回一个迭代器(可迭代对象)<list_reverseiterator object at 0x000001C7E6A0F8C0>
# print(list(reversed(s))) #返回一个反转后的新序列

"""all()和any()函数(返回值为布尔值)""" #all()序列中所有元素都为True则返回True any()序列中有一个元素为True则返回True
# x=[1,1,0]
# y=[1,1,9]
# print(all(x)) #False
# print(any(x)) #True
# print(all(y)) #True
# print(any(y)) #True

"""enumerate()函数""" #返回一个枚举对象(可迭代对象)->也就是迭代器 功能:将序列组合为一个索引序列
# s=["FishC","Python","C","Java"]
# print(list(enumerate(s))) #返回一个枚举对象(可迭代对象)
# print(list(enumerate(s,1))) #返回一个枚举对象(可迭代对象) 从1开始计数
# for i in enumerate(s):
#     print(i)

"""zip()函数""" #返回一个迭代器(可迭代对象) 功能:将多个序列组合为一个索引序列
x=[1,2,3]
y=[4,5,6]
zipped=zip(x,y)
print(list(zipped)) #返回一个迭代器(可迭代对象)
z=[7,8,9]
print(list(zip(x,y,z))) #返回一个迭代器(可迭代对象)

z="FishC"
print(list(zip(x,y,z))) #长度取最短的那个为准

# """import itertools"""
# import itertools
# print(list(itertools.zip_longest(x,y,z))) #长度取最长的那个为准

"""map()函数""" #返回一个迭代器(可迭代对象) 功能:将函数映射到每个序列的每个元素上
# mapped=map(ord,"FishC") #返回一个迭代器(可迭代对象)
# print(list(mapped)) #返回一个迭代器(可迭代对象)

# mapped=map(pow,[2,3,10],[5,2,3]) #返回一个迭代器(可迭代对象) pow(x,y)返回x的y次方 
# print(list(mapped))

"""filter()函数""" #返回一个迭代器(可迭代对象) 功能:过滤序列中的元素
# print(list(filter(str.islower,"FishC"))) #返回一个迭代器(可迭代对象) islower()判断字符串是否都是小写字母



"""迭代器VS可迭代对象""" #可迭代对象可以重复使用 而迭代器则是一次性的
#一个迭代器肯定是一个可迭代对象
# 可迭代对象:可以直接作用于for循环的对象统称为可迭代对象
# 迭代器:可以被next()函数调用并不断返回下一个值的对象称为迭代器

# mapped=map(ord,"FishC") #返回一个迭代器(可迭代对象) 列表这些就是可迭代对象
# for each in mapped:
#     print(each)
# print(list(mapped)) #迭代器只能使用一次

# x=[1,2,3,4,5]
# print(type(x)) #列表
# y=iter(x)
# print(type(y)) #迭代器
# print(next(y)) #迭代器只能使用一次
# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# z=iter(x)
# print(next(z,"not found")) #如果迭代器没有元素了 就返回"not found"
# print(next(z,"not found")) 
# print(next(z,"not found")) 
# print(next(z,"not found")) 
# print(next(z,"not found")) 
# print(next(z,"not found")) 