""" #分支结构"""
""" #1"""
# if 3<5:
#     print("我在里面")
# print("我在外面")

""" #2"""
# if "小甲鱼"=="小姐姐":
#     print("yes")
# else:
#     print("no")

""" #3"""
# try:
#     score = int(input("请输入一个数:"))
# except ValueError:
#     print("输入无效。请输入一个有效的整数。")
# if 0<=score<60:
#     print("D")
# elif 60<=score<80:
#     print("C")
# elif 80<=score<90:
#     print("B")
# elif score>=90:
#     print("A")

""" #4"""
# try:
#     score = int(input("请输入一个数:"))
# except ValueError:
#     print("输入无效。请输入一个有效的整数。")
# if 0<=score<60:
#     print("D")
# elif 60<=score<80:
#     print("C")
# elif 80<=score<90:
#     print("B")
# elif 90<=score<=100:
#     print("A")
# else:
#     print("请输入0-100的数^-^")

""" #5 条件成立执行的语句 if contion else 条件不成立执行的语句"""
# age=16
# print("抱歉 未满18岁禁止访问") if age<18 else print("welcome to the website^o^")
# a=3
# b=5
# # if a<b:
# #     small=a
# # else:
# #     small=b
# small=a if a<b else b
# print(small)

# score=66
# level=('D' if 0<=score<60 else
#        'C' if 60<=score<80 else
#        'B' if 80<=score<90 else
#        'A' if 90<=score<=100 else
#        "请输入0-100的数^-^")
# print(level)

"""分支嵌套"""
# age=18
# ismale=True
# if age<18:
#     print("未满18岁 禁止访问")
# else:
#     if ismale:
#         print("任君选购^-^")
#     else:
#         print("抱歉 本店商品不适合小公举哦~")

"""循环   while for两种循环 break语句 continue语句"""
"""无论是break还是continue语句 只能作用于一层循环体"""
# love="yes"
# while love=="yes":
#     love=input("今天你还爱我吗:")
#     print(love)

# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

"""break语句"""
# while True:
#     answer=input("主人,我可以退出循环了吗?")
#     if answer=="可以":
#         break
#     print("哎 好累~")

"""continue语句"""
# i=0
# while i<10:
#     i+=1i
#     if i%2==0:
#         continue
#     print(i)

"""else语句在循环中""" #else语句可以非常任意的检测到循环的退出状况
# i=1
# while i<5:
#     print(f"循环内 {i}")
#     if i==2:
#         break  #请注意break跳出时循环条件是成立的 不会执行else语句
#     i+=1
# else:
#     print(f"循环外 {i}")

"""else语句应用"""
# day=1
# while day<=7:
#     answer=input("今天有好好学习吗?")
#     if answer!="有":
#         break
#     day+=1
# else:
#     print("恭喜你 已坚持七天")

"""循环的嵌套""" #打印九九乘法表
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{i}*{j}={i*j}",end="\t")
#         j+=1
#     print()
#     i+=1
    
"""for循环"""
"""
    for 变量 in 可迭代对象:(可迭代对象就是指那些元素能够被提取出来的对象 比如字符串)
        statement(s)
"""
# for each in "china":
#     print(each)

"""
   range(stop)
   range(start,stop)
   range(start,stop,step) #都是左闭右开
"""
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

"""找10以内的素数"""
# for i in range(2,10):
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"不是一个素数")
#             break
#     else:
#         print(i,"是一个素数")


