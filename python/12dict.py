"""字典"""#(主要是针对映射关系的情况) dict (key,value) 通过key来实现写入和存取
"""字典是python中唯一实现映射关系的内置类型"""

"""了解字典"""
#创建

# x={"吕布":"口口布","关羽":)"关习习"}
# print(type(x)
#访问

# print(x["吕布"])

#增加
# x["刘备"]="刘baby"
# print(x)

"""创建字典的六种方法"""
"""1"""#赋值定义法
# a={"吕布":"口口布","关羽":"关习习","刘备":"刘baby"}
# print(a)
"""2"""#此处key不能加引号
# b=dict(吕布="口口布",关羽="关习习",刘备="刘baby")
# print(b)
"""3""" #用列表(列表里面包含元组)
# c=dict([("吕布","口口布"),("关羽","关习习"),("刘备","刘baby")])
# print(c)
"""4"""#直接传个字典就是
# d=dict({"吕布":"口口布","关羽":"关习习","刘备":"刘baby"})
# print(d)
"""5"""#混合
# e=dict({"吕布":"口口布","关羽":"关习习"},刘备="刘baby")
# print(e)
"""6"""#用zip函数
# f=dict(zip(["吕布","关羽","刘备"],["口口布","关习习","刘baby"]))
# print(f)

# print(a==b==c==d==e==f)

"""字典的增删改查"""
"""增"""
"""
   fromkeys(iterable[,value]) 可用于快速初始化一个字典 使用iterable指定的可迭代对象来创建一个新的字典,并将所有的值初始化为values参数指定的值
"""
# d=dict.fromkeys("FishC",250)
# print(d)
# d['F']=70
# print(d)
"""删"""
"""
pop() 删除字典一个键值对并返回该键值 如果pop一个不存在的key会报错
popitem() 删除最后一个键值对并返回该键值对
del 删除指定的键值对 如果删除不存在的key会报错 可以删除整个字典 字典变量不存在
clear() 清空字典 但字典变量还在
"""
# d=dict.fromkeys("FishC",250)
# tmp=d.pop('s')
# print(tmp)
# tmp=d.popitem()
# print(tmp)
# del d['i']
# print(d)
# d.clear()
# print(d)

"""改"""
"""
   update([other]) 将other中的键值对添加到字典中 如果键已经存在则覆盖
"""
d=dict.fromkeys("FishC",250)
d['s']=115
d.update({'i':105,'h':104})
print(d)

"""查"""
"""
   get(key[,default]) 获取指定key的值 如果key不存在则返回default
   setdefault(key[,default]) 如果key不存在则添加key并设置其值为default
   items() 返回字典中所有的键值对
   keys() 返回字典中所有的键
   values() 返回字典中所有的值
   copy() 返回字典的浅拷贝
   len() 返回字典中键值对的数量
   in /not in 判断key是否在字典中
   list() 返回字典中所有的键
   iter() 返回字典中所有的键
   reversed() 对字典内部的键值对进行逆向操作  python3.8之后才支持
"""
# d=dict.fromkeys("FishC",250)
# print(d['C'])
# print(d.get('c',"不存在"))
# d.setdefault('C',"code")
# print(d)
# d.setdefault('c',"code")
# print(d)

"""keys,values,items三者是视图对象 会随着字典变化而变化"""
# d=dict.fromkeys("FishC",250)
# d['F']=300
# keys=d.keys()
# values=d.values()
# items=d.items()
# print(items)
# print(keys)
# print(values)

# d.pop('C')
# print(items)
# print(keys)
# print(values)

# e=d.copy()
# print(e)

# print(len(d))

# print('C' in d)
# print('c' not in d)

# print(list(d)) #相当于list(d.keys()
# print(list(d.values()))

# e=iter(d) #获取一个迭代器对象
# print(next(e)) 
# print(next(e))
# print(next(e))
# print(next(e))

# print(list(reversed(d.values()))) #python3.8之后才支持

"""嵌套"""
# d={"吕布":{"语文":60,"数学":70,"英语":80},"关羽":{"语文":90,"数学":80,"英语":70}}
# print(d)
# print(d['关羽']['数学'])

# d={"吕布":[60,70,80],"关羽":[90,80,70]}
# print(d)
# print(d['关羽'][1])

"""字典推导式"""
# d={'F':70,'i':105,'s':115,'h':104,'C':67}
# b={v:k for k,v in d.items()}
# print(b)
# c={v:k for k,v in d.items() if v>100}
# print(c)
# d={x:ord(x) for x in "FishC"}
# print(d)

# d={x:y for x in [1,3,5] for y in [2,4,6]} #嵌套循环 #记住key不能重复
# print(d)