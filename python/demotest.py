# x, n = map(int, input().split())
# total_distance = 0
# days_passed = 0
# while days_passed < n:
#     if (x + days_passed) % 7 in [1, 2, 3, 4, 5]:
#         total_distance += 250
#     days_passed += 1
# print(total_distance)

# n=int(input())
# mylist=list(map(int,input().split()))
# res=[0]
# cnt=0
# for i in range(1,n):
#     cnt=0
#     for j in range(i-1,-1,-1):
#         if mylist[i]>mylist[j]:
#             cnt+=1
#     res.append(cnt)
# print(*res)

# import sys
# n=int(input())
# m=(input())
# flag=0
# cnt=0
# temp=m[::-1]
# if m==m[::-1]:
#     print(cnt)
#     sys.exit(0)
# while flag==0:
#     sum=str(int(m)+int(temp));
#     cnt+=1
#     if cnt>=30:
#         print("Impossible!")
#         break
#     if sum==sum[::-1]:
#         flag=1
#         break
#     m=sum
#     temp=m[::-1]
# if flag==1:
#     print("STEP={}".format(cnt))

# s=input()
# s=s.swapcase()
# print(s)

# n=int(input())
# mylist=[]
# for i in range(n):
#     temp=int(input())
#     mylist.append(temp)
# print(max(mylist))
# print(min(mylist))
# avg=sum(mylist)/len(mylist)
# # print(round(avg,2))
# print("{:.2f}".format(avg))

# a,b,n=map(int,input().split())
# wtime=1
# day=0
# sum=0
# temp=n//(5*a+2*b)
# # print(temp)
#
# sum=temp*(5*a+2*b)
# # print(sum)
#
# # n=n-temp*(5*a+2*b)
# # print(n)
#
# while sum<n:
#     if wtime%7 in [1,2,3,4,5]:
#         sum+=a
#     if wtime%7 in [0,6]:
#         sum+=b
#     wtime+=1;
#     day+=1
# print(temp*7+day)

# cnt=0
# for i in range(1,2021):
#     temp=str(i)
#     cnt+=temp.count('2')
# print(cnt)

# def solve(a,b):
#     while a!=b:
#      if a>b:
#         a=a-b
#      else:
#          b=b-a
#     return a
#
# cnt=0
# for i in range(1,2020):
#     for j in range(i+1,2021):
#         if solve(i,j)==1:
#             cnt+=1
# print(cnt)

# temp=1
# for i in range(1,20):
#     temp+=i*4
#     print(temp)

# mylist=[624,0,761,0,0]
# print(*mylist)

# time_in_milliseconds = int(input())
# seconds = time_in_milliseconds // 1000
# print(seconds)
# hours = seconds // 3600
# print(hours)
# seconds %= 3600
# minutes = seconds // 60
# seconds %= 60
# print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# s=input()
# cnt=0
# for i in range(len(s)-1):
#     for j in range(i+1):
#         temp=s[i:j]
#         for k in range(len(temp)):
#             if temp.count(temp[k]):
#                 cnt+=1
# print(cnt)

# def find_yanghui_index(n):
#     row = 1  # 从第一行开始
#     total_elements = 0  # 总的元素个数
#
#     # 逐行累加元素，直到总数超过或等于 n
#     while total_elements + row < n:
#         total_elements += row
#         row += 1
#
#     # 计算该数字在当前行的位置
#     position_in_row = n - total_elements
#
#     return row, position_in_row
#
# # 示例：
# n = int(input("输入一个n："))
# row, position = find_yanghui_index(n)
# print(f"数字 {n} 位于第 {row} 行的第 {position} 个元素。")

# def max_bush_heights(N):
#     heights = [0] * N
#
#     # 从左到右修剪
#     for i in range(N):
#         heights[i] = i + 1  # 每棵灌木增长的最大高度
#
#     # 从右到左修剪
#     for i in range(N):
#         heights[i] = min(heights[i], N - i)  # 每棵灌木的最大高度由左右修剪确定
#
#     return heights
#
# # 输入
# N = int(input("输入灌木的数量 N："))
# result = max_bush_heights(N)
#
# # 输出结果
# for height in result:
#     print(height)


'''
状态表示：设 dp[i] 表示以第 i 个元素结尾的最长上升子序列的长度。
状态转移：对于每个元素 a[i]，我们需要遍历之前的所有元素 a[j] (j < i)，如果 a[j] < a[i]，则可以将 a[i] 接在 a[j] 之后，此时有 dp[i] = max(dp[i], dp[j] + 1)。
初始条件：每个 dp[i] 初始值为 1，因为每个元素本身可以看作长度为 1 的子序列。
最终结果：遍历所有 dp[i]，找到最大的值。
'''

# def lis_length(arr):
#     n = len(arr)
#     dp = [1] * n  # 初始化 dp 数组，每个位置的初始值为 1
#
#     # 动态规划求解
#     for i in range(1, n):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 # dp[i] = max(dp[i], dp[j] + 1)
#                 if dp[i] < dp[j] + 1:
#                     dp[i] = dp[j] + 1
#
#     # 返回最长上升子序列的长度
#     return max(dp)
#
#
#
#
# # 输入
# n = int(input())  # 读取序列长度
# arr = list(map(int, input().split()))  # 读取序列
#
# # 输出结果
# print(lis_length(arr))

# n=int(input())
# mylist=list(map(str,input().split()))
# mylist=sorted(mylist)[::-1]
# res="".join(mylist)
# print(int(res))

# m,n=map(int,input().split())
# mylist=[]
# for i in range(m,n+1):
#     mylist.append(str(i))
# res="".join(mylist)
# for j in range(10):
#     print(res.count(str(j)),end=" ")

# a,b,c=map(int,input().split())
# print("{:8d} {:8d} {:8d}".format(a,b,c))

# n=int(input())
# print("{:08d}".format(n))

# from functools import cmp_to_key
#
# n = int(input())
# nums = list(map(str, input().split()))
#
# def compare(x, y):
#     num1 = int(str(x)+str(y))
#     num2 = int(str(y)+str(x))
#     return num2 - num1
#
# nums.sort(key = cmp_to_key(compare))
#
# result = ''.join(nums)
# print(int(result))

# def convert_seconds_to_time(n):
#     # 将秒数转换为小时、分钟和秒
#     hour = n // 3600
#     minute = (n % 3600) // 60
#     second = n % 60
#
#     # 格式化输出时间
#     time_str = f"{hour:02d}:{minute:02d}:{second:02d}"
#     print(time_str)
#
# # 从标准输入读取数据
# n = int(input()) // 1000
# n %= 60 * 60 * 24
# convert_seconds_to_time(n)

# s=input()
# s=s.upper()
# print(s)

# n,k=map(int,input().split())
# cnt=0
# for i in range(n+1):
#     temp=str(bin(i))
#     # print(temp[2:])
#     if temp.count('1')==k:
#         cnt+=1
# print(cnt)

# n,t=map(int,input().split())
# temp=list(map(int,list(input())))
# for j in range(t):
#    res=[temp[0]]
#    for i in range(1,n):
#        res.append(temp[i]^temp[i-1])
#    temp=res
# for i in range(len(res)):
#        print(temp[i], end="")


# import math
#
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# count = 0
# for num in range(2, 20210606):
#     if is_prime(num):
#         count += 1
# print(count)

# def count_partitions(target_sum, num_parts):
#     # 初始化 dp 数组
#     dp = [[0] * (target_sum + 1) for _ in range(num_parts + 1)]
#
#     # 边界条件
#     dp[0][0] = 1
#
#     # 状态转移
#     for i in range(1, num_parts + 1):
#         for j in range(1, target_sum + 1):
#             for k in range(1, j + 1):
#                 if i == 1 or k > j - k:
#                     dp[i][j] += dp[i - 1][j - k]
#
#     return dp[num_parts][target_sum]
#
#
# # 参数设置
# target_sum = 2022
# num_parts = 10
#
# # 计算结果
# result = count_partitions(target_sum, num_parts)
# print(result)


# s=input()
# mylist=[]
# for i in range(len(s)):
#     if s[i]>='0' and s[i]<='9':
#         mylist+=list("number")
#     else:
#         mylist.append(s[i])
# res=''.join(mylist)
# print(res)

# for i in range(10):
#     print(i)
# print(i)

# s="hello"
# mylist=list(s)
# print(mylist)

# mylist=['m','y','t']+['j','j','y']
# print(mylist)

# digits=[1,2,3]
# digits = [str(i) for i in digits]
# print(digits)
# s = ''.join(digits)
# print(s)
# nums = int(s)+1
# mylist = list(str(nums))
# mylist=[int(i) for i in mylist]
# print(mylist)

# mylist=[1,1,2,2,3,3,4,5,5,6,7]
# low=1
# res=[mylist[0]]
# for fast in range(1,len(mylist)):
#     if mylist[fast]!=mylist[fast-1]:
#         res.append(mylist[fast]);
#         low+=1
# print(res)
# print(len(res))

#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, value):
#         """在链表末尾添加一个新节点"""
#         if not self.head:
#             self.head = Node(value)
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = Node(value)
#
#     def prepend(self, value):
#         """在链表开头添加一个新节点"""
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#
#     def delete(self, value):
#         """删除链表中值为value的节点"""
#         current = self.head
#         previous = None
#         while current:
#             if current.value == value:
#                 if previous:
#                     previous.next = current.next
#                 else:
#                     self.head = current.next
#                 return True
#             previous = current
#             current = current.next
#         return False
#
#     def print_list(self):
#         """打印链表中的所有元素"""
#         current = self.head
#         while current:
#             print(current.value, end=" -> ")
#             current = current.next
#         print("None")
#
# # 使用示例
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.print_list()  # 输出: 1 -> 2 -> 3 -> None
#
# ll.prepend(0)
# ll.print_list()  # 输出: 0 -> 1 -> 2 -> 3 -> None
#
# ll.delete(2)
# ll.print_list()  # 输出: 0 -> 1 -> 3 -> None


# def solve(n):
#     if n==0:
#        return 1
#     else:
#         return n*solve(n-1)
# n=int(input())
# print(solve(n))

# mylist=[1,2,3,4,4]
# mylist=[str(i) for i in mylist]
# print(','.join(mylist))

# n=int(input())
# d=dict()
# for i in range(1,1+n):
#     d[i]=i*i
# print(d)

# s=input().split(',')
# mylist=list(s)
# mytuple=tuple(mylist)
# print(mylist,end="")
# print(mytuple)

# class output(object):
#     def __init__(self):
#         self.s=""
#     def getstring(self):
#         self.s=input()
#     def outstring(self):
#         print(self.s.upper())
#
# mystr=output()
# mystr.getstring()
# mystr.outstring()

# import math
# num=math.sqrt(eval(input()))
# print(num)

# import math
# c=50
# h=30
# res=[]
# data=list(map(int,input().split(',')))
# for d in data:
#     res.append(round(math.sqrt((2*c*d)/h)))
# res=[str(i) for i in res]
# print(','.join(res))

# x,y=map(int,input().split(','))
# res=[[0]*y for i in range(x)]
# for i in range(x):
#     for j in range(y):
#         res[i][j]=i*j
# print(res)

# mylist=list(map(str,input().split(',')))
# mylist.sort()
# print(','.join(mylist))

# mylist=list(map(str,input().split()))
# myset=set(mylist)
# print(myset)
# mylist=list(myset)
# mylist.sort()
# print(' '.join(mylist))

# mylist=list(map(str,input().split(',')))
# mylist=[int(i,2) for i in mylist]
# # print(mylist)
# for i in mylist:
#     if i%5==0:
#         print(bin(i)[2:])

# s=input()
# print(s[0].isalpha())
# print(s[1].isdigit())

# a,n=map(int,input().split())
# res=0
# temp=0
# for _ in range(n):
#       temp=temp*10+a
#       print(temp)
#       res+=temp
# print(res)

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

# def repeat(num_times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet(name):
#     print(f"Hello {name}!")
#
# greet("World")

# def fun():
#     return 1,2,3
#
# res=fun()
# print(type(res))
# print(res)

# def fun(a,b):
#     return a+b+c
#
# c=100
# print(fun(10,20))
#
#
#
# mytuple=(1,2,3)
# a,b,c=mytuple
# print(a,b,c)

# lst = [
#     {'name': 'myt', 'grade': 100},
#     {'name': 'and', 'grade': 60},
#     {'name': 'is', 'grade': 80}
# ]
# lst.sort(key=lambda x: x['grade'],reverse=True)
# print(lst)
#
# print(type(ord('a')))
# print("最大值:",abs(-100))
#
#
# mylist=[1,2,3,4,5]


# s=input()
# res={chr(i):0 for i in range(ord('a'),ord('z')+1)}
# for i in s:
#     res[i]+=1
# max_key=max(res,key=res.get)
# print(max_key)
# print(res[max_key])

# n=int(input())
# lst=[]
# for i in range(n):
#   temp=int(input())
#   lst.append(temp)
# # print(lst)
# a=0
# b=0
# for j in range(n):
#     if lst[j]>=60:
#         a+=1
#     if lst[j]>=85:
#         b+=1
# print(str(round(a/n*100))+'%')
# print(str(round(b/n*100))+'%')

# mydict = {str(i): 2021 for i in range(0, 10)}
# i = 1
# while True:
#     temp = str(i)
#     for j in temp:
#         mydict[j] -= 1
#     # 检查是否有任何值小于等于0
#     if any(value <= 0 for value in mydict.values()):
#         break
#     i += 1
# print(i)

# import math
#
# n = int(input())
# sum_a = 0
# s = list(map(int, input().split()))
#
# for i in range(n):
#     sum_a += math.factorial(s[i])  # 使用math.factorial代替递归
#
# res = 0
# for i in range(1, 1000):
#     if sum_a % math.factorial(i) != 0:
#         res = i-1
#         break
#
# print(res)


# mydict={'x':90,'y':10,'t':80}
# mydict=list(mydict.items())
# mydict.sort(key=lambda x:x[1])
# print(mydict)

# s="helloworld"
# print("{:*>20s}".format(s))
# print(hex(2))
# print(oct(2))

# mylist=list(map(lambda x:x.upper(),input().split()))
# print(mylist)
# mydict={'x':90,'y':10,'t':80}
# mydict=list(mydict.items())
# mydict.sort(key=lambda x:x[1])
# print(mydict)
# print(id(mydict))

# s="myhei1234sdf"
# res=0
# for i in s:
#     if i.isdigit():
#         res+=int(i)
# print(res)

# n=int(input())
# n=n//1000
# n=n%(60*60*24)
# a=n//3600
# if a<10:
#     print('0',end="")
# print(str(a)+':',end="")
# b=(n%3600)//60
# if b<10:
#     print('0',end="")
# print(str(b)+':',end="")
# c=n%60
# if c<10:
#     print('0',end="")
# print(str(c))

# n=int(input())
# m=int(input())
# mydict={i:0 for i in range(1,n+1)}
# for j in mydict.keys():
#     mylist=list(map(int,str(j)))
#     temp=sum(mylist)
#     mydict[j]=temp
# mydict=list(mydict.items())
# # print(mydict)
# mydict.sort(key=lambda x:x[1])
# # print(mydict)
# print(mydict[m-1][0])

# def solve(n):
#   if n<2:
#     return False
#   if n==2:
#       return True
#   flag=1
#   for i in range(2,n//2+1):
#     if n%i==0:
#       flag=False
#       break
#   return flag
#
# res=0
# lst=[]
# for i in range(2,1000000):
#     if solve(i):
#         temp=list(map(int,str(i)))
#         if all([solve(j) for j in temp]):
#            lst.append(i)
#            res+=1
# print(lst)
# print(res)

# n,k=map(int,input().split())
# # print(n,k)
# res=0
# for i in range(1,n+1):
#   temp=list(map(int,str(bin(i)[2:])))
#   # print(temp)
#   if temp.count(1)==k:
#      res+=1
# print(res)


# n=int(input())
# lst=[]
# for i in range(2,10):
#   temp=int(n*i)
#   # print(temp)
#   temp=str(bin(temp))[2:]
#   # print(temp)
#   lst.append(temp.count('1'))
#   # print(lst)
# print(min(lst))

# s=input()
# n=int(input())
# for i in range(n):
#   l, r, x, y = input().split()
#   # print(l,r,x,y)
#   for j in range(int(l)-1,int(r)):
#     if s[j]==x:
#       s=s[:j]+y+s[j+1:]
#   # print(s)
# print(s)


# n=int(input())
# lst=list(map(int,input().split()))
# res=0
# if lst[1]!=lst[0]:
#   lst[1]=lst[0]
#   res+=1
# # print(lst)
# for i in range(2,n):
#     if lst[i]!=(lst[i-1]+lst[i-2]):
#       lst[i]=lst[i-1]+lst[i-2]
#       # print(lst[i])
#       res+=1
# print(res)
# # print(lst)

# def solve(n):
#   if n<2:
#     return 0
#   for i in range(2,int(n//2+1)):
#     if n%i==0:
#       return 0
#   return 1
#
# n=int(input())
# res=0
# for i in range(2,int(n//2+1)):
#   if solve(i):
#     if n%i==0:
#        print(i)
#        res+=1
# print(res)

# import math
# n=int(input())
# lst=list(map(int,input().split()))
# temp=0
# for i in lst:
#   temp+=math.factorial(i)
# # print(temp)
# res=1
# result=math.factorial(res)
# cnt=0
# while(result<=temp):
#   if temp%result==0:
#     cnt=res
#     # print(cnt)
#   res+=1
#   result = math.factorial(res)
#   # print(res,result)
#   # print("-----------")
# print(cnt)

'''
这个实现的工作原理如下：
find_position_in_pascal_triangle 函数从杨辉三角的第一行开始，逐行生成数字。
对于每个生成的数字，我们增加位置计数器 position。
如果生成的数字等于目标数，我们返回当前的位置。
如果生成的数字大于目标数，我们知道目标数不在杨辉三角中，因为杨辉三角中的数字在每一行都是递增的。
calculate_pascal_number 函数使用递归方法计算杨辉三角中特定位置的数字。
如果遍历完整个三角形都没有找到目标数，函数返回 -1，表示目标数不在杨辉三角中。
'''


# def find_position_in_pascal_triangle(target):
#   row = 1
#   position = 1
#   current = 1
#
#   while current < target:
#     row += 1
#     for col in range(1, row + 1):
#       current = calculate_pascal_number(row, col)
#       position += 1
#       if current == target:
#         return position
#       if current > target:
#         return -1  # 目标数不在杨辉三角中
#
#   return -1  # 目标数不在杨辉三角中
#
#
# def calculate_pascal_number(row, col):
#   if col == 1 or col == row:
#     return 1
#   return calculate_pascal_number(row - 1, col - 1) + calculate_pascal_number(row - 1, col)
#
#
# # 测试
# target = int(input())
# result = find_position_in_pascal_triangle(target)
# print(result)


# '''打印杨辉三角'''
# def print_pascal_triangle(n):
#   for i in range(n):
#     for j in range(n - i):
#       print(" ", end=" ")
#     for j in range(i + 1):
#       print()

# s=input()
# s=list(s)
# s.sort()
# print(''.join(s))


# from decimal import Decimal, getcontext
#
# # 设置高精度
# getcontext().prec = 50
#
#
# def count_regions(lines):
#   n = len(lines)
#   intersections = set()
#
#   for i in range(n):
#     for j in range(i + 1, n):
#       a1, b1 = lines[i]
#       a2, b2 = lines[j]
#
#       # 检查是否平行
#       if a1 == a2:
#         continue
#       else:
#         # 计算交点
#         x = Decimal(b2 - b1) / Decimal(a1 - a2)
#         y = Decimal(a1) * x + Decimal(b1)
#         intersections.add((x, y))
#
#   # 计算区域数
#   regions = 1 + n + len(intersections)
#
#   return regions
#
#
# # 读取输入
# n = int(input())
# lines = [tuple(map(int, input().split())) for _ in range(n)]
#
# # 计算并输出结果
# result = count_regions(lines)
# print(result)

# import os
# import sys
# import math
# # 请在此输入您的代码
# def solve(a,b):
#   while(a!=b):
#     if a>b:
#       a=a-b
#     else:
#       b=b-a
#   return a
#
# a,b=map(int,input().split())
# temp=int(math.pow(a,b))
# res=0
# # print(solve(a,b))
# for i in range(1,int(math.pow(a,b))):
#   if solve(i,temp)==1:
#     res+=1
# print(res%998244353)

# def get_number_at_position(pos):
#   # 计算当前位置所在的组
#   group = 1
#   group_start = 1
#   while group_start + group <= pos:
#     group_start += group
#     group += 1
#
#   # 计算在组内的位置
#   in_group_pos = pos - group_start + 1
#
#   return in_group_pos
#
#
# def sum_range(l, r):
#   total = 0
#   for i in range(l, r + 1):
#     total += get_number_at_position(i)
#   return total
#
#
# # 读取输入
# T = int(input())
# queries = [list(map(int, input().split())) for _ in range(T)]
#
# # 处理每个查询并输出结果
# for l, r in queries:
#   result = sum_range(l, r)
#   print(result)

# def find_nth_number(n):
#   # 确定段落
#   k = 1
#   while k * (k + 1) // 2 < n:
#     k += 1
#
#   # 计算具体位置
#   pos = n - (k * (k - 1) // 2)
#
#   # 返回具体数值
#   return pos
#
# n=int(input())
# lst=[]
# for i in range(n):
#   temp=list(map(int,input().split()))
#   lst.append(temp)
# # print(lst)
# for i in range(n):
#   res=0
#   m=lst[i][0]
#   n=lst[i][1]
#   for j in range(m,n+1):
#     res+=find_nth_number(j)
#   print(res)

# def print_all_substrings(s):
#   length = len(s)
#   for i in range(length):  # 外层循环遍历起始位置
#     for j in range(i + 1, length + 1):  # 内层循环遍历结束位置
#       print(s[i:j])
#
#
# # 测试字符串
# test_string = "abc"
# print_all_substrings(test_string)

# def solve(n):
#   if n==0:
#     return "0"
#   res=""
#   while n>0:
#     temp=n%4
#     res=str(temp)+res
#     n=n//4
#   return res

# cnt=0
# for i in range(1,2025):
#   a=list(map(int,bin(i)[2:]))
#   b=list(map(int,solve(i)))
#   if sum(a)==sum(b):
#     cnt+=1
# print(cnt)

# n,m=map(int,input().split())
# lst=[]
# for i in range(n):
#   temp=list(map(int,input().split()))
#   lst.extend(temp)
# # print(lst)
# cnt=0
# for i in range(len(lst)):
#   for j in range(i+1,len(lst)):
#     # print(i, j)
#     if lst[i]==lst[j]:
#        a=i//m
#        b=i%m
#        c=j//m
#        d=j%m
#        # print(a,b,c,d)
#        if abs(a-c)==abs(b-d):
#          cnt+=1
# print(cnt*2)

# n=int(input())
# lst=[]
# for i in range(n):
#   temp=input()
#   lst.append(temp)
# # print(lst)
# res=lst[0]
# for i in range(1,n):
#     if res[len(res)-1]==lst[i][len(lst[i])-1]:
#       tmp=lst[i][::-1]
#       # print(tmp)
#       length=len(tmp)
#       res+=lst[i][0:length-1]
#     else:
#       res+=lst[i]
# print(len(res))

# def multiply():
#     return [lambda x: i * x for i in range(4)]
#
# print([m(100) for m in multiply()])

# lst=input().split()
# print(lst)

# n=int(input())
# lst=[]
# for i in range(n):
#   temp=list(map(int,input().split()))
#   lst.append(temp)
# print(lst)

import os
import sys

# 请在此输入您的代码
# from datetime import *
# s = datetime(1900, 1, 1)
# e = datetime(9999, 12, 31)
# t = timedelta(days=1)
# print(t)
# # now=datetime.now()
# # print(now)
# summ = 0
# while s < e:
#     y = int(s.year)
#     m = int(s.month)
#     d = int(s.day)
#     # print(y,m,d)
#     n = y//1000 + ((y//10) % 10) + y % 10 + ((y//100) % 10)
#     m = m % 10 + m//10 + d % 10 + d//10
#     if m == n:
#         summ += 1
#     s += t
# print(summ)
# print(70910)

# n = int(input())
# s = [0] + list(input())
#
# dp = [[0]*3 for _ in range(n+1)]
#
# for i in range(1,n+1):
#   dp[i][0] = dp[i-1][0] + int(s[i])
#   dp[i][1] = max(dp[i-1][0],dp[i-1][1])+(int(s[i])^1)
#   dp[i][2] = max(dp[i-1][1],dp[i-1][2])+int(s[i])
#
# print(max(dp[n]))


# s = input()
# temp=s
#
# substrings = []
# n = len(s)
#
# lst=[]
# # 遍历所有可能的子串
# for i in range(n):
#   for j in range(i + 1, n + 1):
#     s=temp
#     substr = s[i:j]
#     replaced_substr = ''.join(['1' if c == '0' else '0' for c in substr])
#     s = s[:i] + replaced_substr + s[j:]
#     lst.append(s.count('1'))
# print(max(lst))

# import datetime
#
# start = datetime.datetime(2000, 1, 1)
# end = datetime.datetime(2020, 10, 1)
# days = datetime.timedelta(days=1)
# ans = 0
#
# while end >= start:
#     if start.day == 1 or start.weekday() == 0:
#         ans += 2
#     else:
#         ans += 1
#     start += days
# print(ans)

# # 引入 datetime 模块
# import datetime
#
# # datetime模块的变量
# max_year = datetime.MAXYEAR # 9999
# print(max_year)
#
# # 用法一
# # 使用 datetime类 的方法
# today = datetime.datetime.today() # 这个方法在类中而不是外层模块中
# print(today)
#
# # 用法二
# # 实例化 datetime 对象，年月日必填
# #[year, month, day, hour, minute, second, microsecond]
# # d = datetime.datetime(2024, 6, 1) # 两个 datetime !! 第一个是模块，第二个是模块里面同名的类
# # print(d)
#
# # 创建一个日期时间对象
# d = datetime.datetime(2024, 10, 10, 0, 0, 0)
#
# # 替换年份
# d = d.replace(year=2020)
# d = d.replace(day=30)
# # 打印结果
# print(d.month)
#
# dt = datetime.datetime(2021, 1, 1, 0, 0, 0)
# datetimeStr = dt.strftime('%Y-%m-%d %H:%M:%S')
# print(datetimeStr)

# import datetime
#
# start=datetime.date()

# from datetime import datetime,timedelta
#
# start=datetime(2000,1,1)
# end=datetime(2020,10,1)
#
# temp=timedelta(days=1)
#
# res=0
#
# while end>=start:
#   if start.day==1 or start.weekday()==0:
#     res+=2
#   else:
#     res+=1
#   start+=temp
#
# print(res)
#
# import datetime
#
# start = datetime.datetime(2000, 1, 1)
# end = datetime.datetime(2020, 10, 1)
# days = datetime.timedelta(days=1)
# ans = 0
#
# while end >= start:
#     if start.day == 1 or start.weekday() == 0:
#         ans += 2
#     else:
#         ans += 1
#     start += days
# print(ans)

# from datetime import datetime
#
# # 给定的日期时间字符串
# date_string = "2023-03-15 14:22:00"
#
# # 定义日期时间格式
# date_format = "%Y-%m-%d %H:%M:%S"
#
# # 解析字符串为 datetime 对象
# date_object = datetime.strptime(date_string, date_format)
#
# print(date_object)
# print(type(date_object.year))
# print(type(date_object))

# from datetime import datetime,timedelta
#
# start=datetime(1900,1,1)
# end=datetime(9999,12,31)
#
# temp=timedelta(days=1)
#
# res=0
# while start<=end:
#   lst1=list(map(int,str(start.year)))
#   lst2=list(map(int,str(start.month)+str(start.day)))
#   if sum(lst1)==sum(lst2):
#     res+=1
#   start+=temp
#
# print(res)
#
# from datetime import datetime, timedelta
#
# # 设置日期范围的起始和结束时间
# start = datetime(1900, 1, 1)
# end = datetime(9999, 12, 31)
#
# # 定义一天的时间增量
# temp = timedelta(days=1)
#
# # 初始化计数器
# res = 0
#
# # 遍历指定日期范围内的每一天
# while start <= end:
#     # 将年份转换为数字列表并求和
#     lst1 = list(map(int, str(start.year)))
#     # 将月份和日期拼接后转换为数字列表并求和
#     lst2 = list(map(int, str(start.month) + str(start.day)))
#
#     # 检查两组数字之和是否相等
#     if sum(lst1) == sum(lst2):
#         res += 1
#
#     if start==datetime(9999,12,31):
#       break
#     # 进入下一天
#     start += temp
#
#
# # 输出满足条件的日期总数
# print(res)

def min_operations(nums, k):
    n = len(nums)
    operations = 0

    # 计算每个位置及其后的 K-1 个位置上的元素之和
    for i in range(n - k + 1):
        # 检查当前位置及其后的 K-1 个位置上的元素之和是否大于 0
        if all(num > 0 for num in nums[i:i + k]):
            # 减去 K 个元素
            for j in range(i, i + k):
                nums[j] -= 1
            operations += 1

    # 处理剩下的不足 K 个元素
    for i in range(n - k + 1, n):
        if nums[i] > 0:
            nums[i] -= 1
            operations += 1

    return operations


# 读取输入
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# 计算并输出结果
result = min_operations(nums, k)
print(result)
