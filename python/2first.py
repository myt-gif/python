"""用python设计第一个小游戏""" #长字符串 相当于程序的说明文档
import random

#设置循环次数
count=3

#生成随机数

answer=random.randint(1,10)

# #实现对伪随机数的攻击(补充)
# x=random.getstate() #获取随机数的种子
# """输入一定的数"""
# random.setstate(x)
# """此时再生成的随机数就是先前输入的"""

#猜数
while count>0:
  temp=input("不妨猜一下小甲鱼现在心里想的哪个数:")
  guess=int(temp)

  if guess==answer:
    print("猜对了")
    break
  else:
    if guess<answer:
        print("小啦~")
    else:
        print("大啦~")
  count=count-1

print("游戏结束 不玩了^-^")