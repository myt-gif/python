"""列表""" #list 无序 可变
"""切片对于所有的序列都实用"""
"""序列: 字符串,列表,元组等都是序列 可用于for循环"""
"""列表是可变的 字符串是不可变的"""
# a=[1,2,3,4,5]
# print(a)

"""列表可以容纳不同类型的数据"""
# a=[1,2,3,4,5,"上山打老虎"]
# print(a)
# for i in a:
#     print(i)

"""下标索引""" #注意python中下标可逆序 即最后一个元素下标为-1 倒数第二个为-2 以此类推
# a=[1,2,3,4,5,"上山打老虎"]
# length=len(a)
# print(a[length-1])
# print(a[-1])

"""列表切片""" #a[start:stop:step]
# a=[1,2,3,4,5,"上山打老虎"]
# print(a[0:3])  #输出0-2的元素 左闭右开
# print(a[:3]) #输出最开始到下标为2
# print(a[3:]) #输出下标为3到最后
# print(a[:]) #输出全部
# print(a[0:6:2])
# print(a[::2])
# print(a[::-2])
# print(a[::-1]) #列表倒序输出

"""列表的诸多方法(增删改查)"""
"""增""" #append(元素) 在列表的末尾来添加一个指定的元素 每次只能添加一个元素
    #extend(可迭代对象) 添加一个可迭代对象 新的内容是追加到原列表的最后一个元素的后面
    #insert(待插入的位置,待插入的元素) 在列表的任意位置插入元素
# heros=["钢铁侠","绿巨人"]
# heros.append("黑寡妇")
# print(heros)
# heros.extend(["鹰眼","灭霸","雷神"])
# print(heros)

# a=[1,2,3,4,5]
# a[len(a):]=[6] #相当于a.append(6)到最后
# print(a)
# a[len(a):]=[7,8,9] #相当于a.extend([7,8,9])到最后
# print(a)

# s=[1,3,4,5]
# s.insert(1,2)
# print(s)

"""删""" #remove(元素) 值得注意的是,如果列表中存在多个匹配的元素,那么它只会删除第一个
         #pop(索引) 删除指定索引的元素
         #clear() 删除列表的所有元素
# heros=["钢铁侠","绿巨人","鹰眼","灭霸","雷神"]
# heros.remove("灭霸")
# print(heros)
# heros.pop(len(heros)-1)
# print(heros)
# heros.clear()
# print(heros)

"""改"""
# heros=["钢铁侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
# heros[4]="钢铁侠"
# print(heros)
# heros[3:]=["武松","林冲","李逵"] #利用切片修改多个元素
# print(heros)

# nums=[3,1,9,6,8,3,5,3]
# nums.sort()
# print(nums)
# nums.reverse() #先排序 再反转 可实现从大到小排序
# print(nums)

"""查"""
# nums=[3,1,9,6,8,3,5,3]
# print(nums.count(3))
# print(nums.index(3)) #index(元素,start,stop) 指定查找位置
# nums_copy1=nums.copy()  #copy函数进行拷贝 浅拷贝
# print(nums_copy1)
# nums_copy2=nums[:] #切片的方法 浅拷贝
# print(nums_copy2)

"""列表的加法(拼接)和乘法"""
# s=[1,2,3]
# t=[4,5,6]
# print(s+t)
# print(s*3)

"""嵌套列表"""
# matrix=[[1,2,3],[4,5,6],[7,8,9]] #二位列表
# matrix=[[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# print(matrix)
# print(matrix[0])
# print(matrix[0][0])
# #遍历嵌套列表
# for i in  matrix:
#     for each in i:
#         print(each,end=" ")
#     print()

"""重要点 容易出现的bug"""
# A=[0]*3
# print(A)
# for i in range(3):
#     A[i]=[0]*3
# print(A)
# A[1][1]=1
# print(A) #A中的三个列表对应不同的对象
# print(bool(A[1] is A[0])) #is用于判断两个对象是否相等

# B=[[0]*3]*3 #错误写法
# B[1][1]=1
# print(B) #B中的三个列表对应相同的对象
# print(bool(B[1] is B[0]))

# C=[[0]*3 for i in range(3)] #正确写法
# C[1][1]=1
# print(C)

# import copy
"""浅拷贝和深拷贝"""
"""浅拷贝"""
# nums=[3,1,9,6,8,3,5,3]
# nums_copy1=nums.copy()  #copy函数进行拷贝 
# print(nums_copy1)
# nums_copy2=nums[:] #切片的方法
# print(nums_copy2)

"""浅拷贝"""
# import copy  # 导入copy模块

# x=[[1,2,3],[4,5,6],[7,8,9]]  # 定义一个列表x，元素是三个列表
# y=copy.copy(x)  # 使用copy模块的copy函数，将x进行浅拷贝，赋值给y
# x[1][1]=0  # 修改x的第二个列表的第二个元素，将其改为0
# print(x)  # 打印x，输出结果为：[[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# print(y)  # 打印y，输出结果为：[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""深拷贝"""
# import copy

# # 创建一个列表x，包含三个子列表，每个子列表包含三个元素
# x=[[1,2,3],[4,5,6],[7,8,9]]
# # 使用copy模块的deepcopy函数创建一个x的副本y
# y=copy.deepcopy(x)
# # 将x的第二个子列表的第二个元素修改为0
# x[1][1]=0
# # 打印修改后的x
# print(x)
# # 打印副本y
# print(y)

"""列表推导式"""
"""
基本语法:[表达式 for 变量 in 列表 if 条件]  #先执行for循环，再执行if条件，最后执行表达式
        [excession for 变量 in 列表 if 条件]
"""
# 创建一个包含0到9的列表
# x=[i for i in range(10)]
# # 打印这个列表
# print(x)
# # 创建一个包含0到9的列表，每个元素加1
# x=[i+1 for i in range(10)]
# # 打印这个列表
# print(x)
# # 创建一个包含1到9的列表
# nums=[1,2,3,4,5,6,7,8,9]
# # 创建一个包含nums中偶数的列表
# nums1=[i for i in nums if i%2==0]
# # 打印这个列表
# print(nums1)
# # 创建一个包含nums中元素平方的列表
# nums2=[i**2 for i in nums]
# # 打印这个列表
# print(nums2)

# # 创建一个包含字符串'FishC'中每个字符ASCII值的列表
# code=[ord(c) for c in 'FishC']
# # 打印这个列表
# print(code)

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# # 创建一个包含matrix中每个元素平方的列表
# matrix2=[[i**2 for i in row] for row in matrix]
# # 打印这个列表
# print(matrix2)

# 定义一个3x3的矩阵
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# #取出矩阵中第二列的元素，存入col2列表中
# col2=[row[1] for row in matrix]
# #打印col2列表
# print(col2)

# # 定义一个列表diag，存储矩阵matrix的对角线元素
# diag=[matrix[i][i] for i in range(len(matrix))]
# # 打印出列表diag
# print(diag)

# # 定义一个列表diag2，存储矩阵matrix的反对角线元素
# diag2=[matrix[i][len(matrix)-i-1] for i in range(len(matrix))]
# # 打印出列表diag2
# print(diag2)

"""列表推导式"""
# b=[[0]*3]*3
# print(b) # 输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# b[1][1]=1
# print(b) # 输出：[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

# a=[0]*3
# for i in range(3):
#     a[i]=[0]*3
# print(a) # 输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# a[1][1]=1
# print(a) # 输出：[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

# #利用列表推导式
# s=[[0]*3 for i in range(3)]
# print(s) # 输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# s[1][1]=1
# print(s) # 输出：[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

# even=[i for i in range(10) if i%2==0]
# print(even) # 输出：[0, 2, 4, 6, 8]

# words=['FishC','Python','Java','Fan','Great']
# Fword=[i  for i in words if i[0]=='F']
# print(Fword) # 输出：['FishC', 'Fan']

"""嵌套列表推导式(从左往右依次看)"""
"""
   基本语法:[expression for item in list1 for item2 in list2 ... for itemn in listn]
"""
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# flatten=[i for row in matrix for i in row] #外层循环放前面 内存循环放后面 可以从前往后读
# print(flatten) # 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]

"""笛卡尔乘积"""
# 打印出列表，其中x和y分别是'abc'和'123'中的元素，x+y表示将x和y连接起来
# print([x+y for x in 'abc' for y in '123'])

# # 打印出列表，其中x和y分别是0到9的整数，x%2==0表示x是偶数，y%3==0表示y是3的倍数
# print([[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0]) #从左往右依次看
# # 初始化一个空列表result
# result = []
# # 遍历0到10的整数，如果x是偶数，则继续遍历0到10的整数，如果y是3的倍数，则将x和y添加到result列表中
# for x in range(10):
#     if x % 2 == 0:
#         for y in range(10):
#             if y % 3 == 0:
#                 result.append([x, y])
# # 打印出result列表
# print(result)

"""kiss原则:Keep It Simple, Stupid"""
