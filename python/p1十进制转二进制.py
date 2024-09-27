num=(int)(input())
temp=""
while num>0:
    temp+=(str)(num%2) #这里用chr转要处问题? chr(1)这里得数字1并不是转成字符1 而是转成对应得ASCII字符
    num//=2
print(temp[::-1])
