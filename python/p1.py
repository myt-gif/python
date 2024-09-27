l=[]
for i in range(2000,3201):
    if (i%7==0) and (i%2!=0):
       l.append(str(i)) #','.join(l) 中的 l 需要是一个字符串列表
print(','.join(l))