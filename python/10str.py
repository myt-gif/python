"""字符串""" # 特点:不可变

"""判断字符串是否为回文数"""

# x="12321"
# y=x[::-1]
# print(bool(x==y))

"""判断整数是否为回文数"""

# x=12321
# y=str(x)[::-1]
# print(bool(x==int(y)))

"""大小写字母换来换去"""
"""
   capital()将字符串中所有小写字母转换为大写字母
   casefold()将字符串中所有大写字母转换为小写字母  capital函数和casefold()函数既能处理英文，也能处理其它语言
   title()将字符串中每个单词的首字母转换为大写字母
   swapcase()将字符串中所有大写字母转换为小写字母，所有小写字母转换为大写字母
   upper()将字符串中所有小写字母转换为大写字母
   lower()将字符串中所有大写字母转换为小写字母 upper()和lower()函数只能处理英文，不能处理其它语言
"""

# x="I Love FishC"
# y=x.upper() #因为字符串是不可变的，所以返回的是新的字符串
# print(y)
# z=x.lower()
# print(z)
# a=x.title()
# print(a)

"""左中右对齐"""
"""
   center(width,fillchar='')将字符串居中，并使用fillchar填充两侧，使字符串总长度为width
   ljust(width,fillchar='')将字符串左对齐，并使用fillchar填充右侧，使字符串总长度为width
   rjust(width,fillchar='')将字符串右对齐，并使用fillchar填充左侧，使字符串总长度为width
   zfill(width)将字符串右对齐，并使用0填充左侧，使字符串总长度为width
"""

# x="有内鬼，终止交易!"
# print(x.center(5)) #当字符串长度大于5 直接原字符串输出
# print(x.center(15)) #默认填充字符为空格
# print(x.ljust(15))
# print(x.rjust(15))
# print(x.zfill(15))#在做数据报表时，经常需要将数字左对齐，并用0填充右侧
# print("520".zfill(5))
# print("-520".zfill(5)) #负号也算在长度内

"""查找"""
"""
count(sub[,start[,end]])返回字符串中sub出现的次数，start和end指定查找范围
find(sub[,start[,end]])返回字符串中sub第一次出现的索引，如果不存在则返回-1，start和end指定查找范围 从左往右查找
rfind(sub[,start[,end]])返回字符串中sub最后一次出现的索引，如果不存在则返回-1，start和end指定查找范围 从右往左查找
index(sub[,start[,end]])返回字符串中sub第一次出现的索引，如果不存在则抛出异常，start和end指定查找范围
rindex(sub[,start[,end]])返回字符串中sub最后一次出现的索引，如果不存在则抛出异常，start和end指定查找范围
"""

# x="上海自来水来自海上"
# print(x.count("海"))
# print(x.count("海",0,5)) #start和end指定查找范围 ，左闭右开
# print(x.find("海"))
# print(x.rfind("海"))
# print(x.index("海"))
# print(x.rindex("海")) #如果不存在则抛出异常

"""替换"""
"""
   expandtabs([tabsize=8])将字符串中的\t替换为空格，默认为8个空格
   replace(old,new[,count])将字符串中的old替换为new，count指定替换次数 count=-1表示全部替换(默认)
   translate(table,deletechars='')根据table中的字符映射替换字符串中的字符，deletechars指定要删除的字符
"""

# x="hello\tworld"
# print(x.expandtabs(4))
# print(x.replace("o","O",1))
# str="I love FishC"
# table=str.maketrans("ABCDEFG","1234567","love") #创建映射表
# print(str.translate(table)) #将字符串中的字符根据映射表进行替换 I love FishC -> I love 6ish3 将love忽略

"""判断和检测(返回的都是布尔值)"""
"""
   startswith(prefix[,start[,end]])判断字符串是否以prefix开头，start和end指定判断范围
   endswith(suffix[,start[,end]])判断字符串是否以suffix结尾，start和end指定判断范围
   isupper()判断字符串中所有字母是否都为大写
   islower()判断字符串中所有字母是否都为小写
   istitle()判断字符串中所有字母是否都为大写开头
   isalpha()判断字符串中所有字符是否都为字母
   isascii()判断字符串中所有字符是否都为ASCII字符 AsCII字符范围：0-127 包括空格、数字、字母、特殊符号
   isspace()判断字符串中所有字符是否都为空白字符 （空格、制表符、换行符等）都是空白字符
   isprintable()判断字符串中所有字符是否都为可打印字符
   isdecimal()判断字符串中所有字符是否都为十进制字符
   isdigit()判断字符串中所有字符是否都为数字字符
   isnumeric()判断字符串中所有字符是否都为数字字符
   isalnum()判断字符串中所有字符是否都为字母或数字
   isidentifier()判断字符串中所有字符是否都为合法的标识符 合法的标识符：字母、数字、下划线，且不能以数字开头

   isalnum()判断字符串中所有字符是否都为字母或数字
"""
# x="我爱python"
# print(x.startswith("我",0,3))
# print(x.endswith("python",1,8))

"""可以实现多匹配"""
# x="他爱python"
# if x.startswith(("我","你","他")): #此时应该传入一个元组
#     print("匹配成功")   

# x="I love Python\t"
# print(x.istitle()) #判断字符串中所有字母是否都为大写开头
# print(x.isupper()) #判断字符串中所有字符是否都为字母
# print(x.upper().isupper()) #将字符串中所有字母都转换为大写后判断
# print(x.isalpha()) #判断字符串中所有字符是否都为字母
# print(x.isspace())  #判断字符串中所有字符是否都为空白字符
# print(x.isalnum()) #判断字符串中所有字符是否都为字母或数字
# print(x.isidentifier()) #判断字符串中所有字符是否都为合法的标识符 合法标识符：字母、数字、下划线，且不能以数字开头
# print(x.isdecimal()) #判断字符串中所有字符是否都为十进制字符 十进制字符：0-9
# print(x.isdigit()) #判断字符串中所有字符是否都为数字字符 数字字符：0-9、空格、下划线、加号、减号
# print(x.isnumeric()) #判断字符串中所有字符是否都为数字字符
# print(x.isprintable()) #判断字符串中所有字符是否都为可打印字符 (是否包括转义字符)
# print(x.isascii()) #判断字符串中所有字符是否都为ASCII字符

"""判断一个字符串是否为python关键字(if while for 等)"""
# import keyword
# print(keyword.iskeyword("if"))
# print(keyword.iskeyword("python"))

"""截取"""
"""
   单个字符
   strip(char=None) 去除字符串两端的空白字符  默认去除空格 也可以去除指定的字符
   lstrip(char=None) 去除字符串左端的空白字符
   rstrip(char=None) 去除字符串右端的空白字符

   子字符串
   replace(old,'') 将字符串中的old替换为new，count表示替换的次数，默认为-1，表示全部替换去除字符串中指定的字符
   removeprefix() 去除字符串左端的指定字符
   removesuffix() 去除字符串右端的指定字符
"""

"""去除单个字符"""

# print("   左侧不要留白".lstrip(""))
# print("右侧不要留白   ".rstrip())
# print("  左右两侧不要留白  ".strip())
# print("  左右两侧  不要留白  ".strip())
# print("www.ilovefishc.com".lstrip("wcom.")) #去除字符串左端的指定字符 wcom. 注意：wcom.的顺序不能改变 从左侧开始删除 直到遇到第一个不是wcom.的字符为止
# print("www.ilovefishc.com".rstrip("wcom.")) #按照单个字符为单位去匹配剔除的
# print("www.ilovefishc.com".strip("wcom."))

"""去除子字符串"""
# print("www.ilovefishc.com".removeprefix("www."))
# print("www.ilovefishc.com".removesuffix(".com"))
# print("www.ilovefishc.com".replace("love",''))

"""字符串的拆分和拼接"""
"""
   拆分:split()  splitlines()  partition()  rpartition()
        split(切割次数(默认为-1 全切)) 将字符串按照指定的字符拆分成多个子字符串，返回一个列表 默认按照空格拆分
        rsplit(切割次数(默认为-1 全切)) 从右往左去切 将字符串按照指定的字符拆分成多个子字符串，返回一个列表 默认按照空格拆分
        splitlines() 将字符串按照换行符拆分成多个子字符串，返回一个列表 换行符包括：\n \r \r\n
        partition() 从左往右拆分 作用：将字符串按照指定的字符拆分成三部分，返回一个元组 三元组:(第一部分，指定的字符，第二部分)
        rpartition()从右往左拆分 作用：将字符串按照指定的字符拆分成三部分，返回一个元组

        
   拼接:join() 将列表中的元素拼接成一个字符串
   
"""

"""拆分"""
# print("苟日新, 日日新, 又日新".split(",")) #按照逗号拆分
# print("苟日新, 日日新, 又日新".split(",",1))
# print("苟日新, 日日新, 又日新".rsplit(","))

# print("苟日新\n日日新\r又日新".splitlines())

# print("www.ilovefishc.com".partition("."))
# print("www.ilovefishc.com".rpartition("."))

"""拼接"""
# print("-".join(["www","ilovefishc","com"]))  #使用join()方法比使用"+"拼接字符串效率更高



"""格式化字符串的方法""" # {位置或者关键字索引:格式化选项}
# year=2024
# print("今年是{:d}年".format(year))
# a=3.1215926
# print("圆周率是{:.2f}".format(a))
# print("1+2={:d},2的平方是{:d},3的立方是{:d}".format(1+2,2**2,3**3))

# print("{:s} love {:s}".format("I","you"))
# print("{1} love {0}".format("I","you"))

# print("{0}{0}{1}{1}".format("是","非"))

# print("我叫{name},我爱{fav}".format(name="张三",fav="鱼C"))

"""align对齐"""
# print("{:^10}".format(520)) #居中
# print("{1:>10}{0:<10}".format(520,1314)) #右对齐 左对齐
# print("{:010}".format(520)) #补零 只对于整数有效

"""sign符号选项"""
# print("{:+d} {:-d}".format(520,-250))
"""千位的分割符"""
# print("{:,}".format(1234567890))

"""m:n"""
# print("{:.2f}".format(3.1415))
# print("{:.2g}".format(3.1415))

"""输出进制数"""
# print("{:#b}".format(10)) #二进制 :b只能用于整数

"""十进制整数转换成二进制整数"""
# print(bin(10))
"""十进制小数转换成二进制小数"""
"""注意这里只能输入小于1的小数"""
# data = float(input("请输入一个小于1的小数："))
# tmp = data
# res = '0.'
# while tmp != 0:
#     z = int(tmp * 2)
#     res += str(z)
#     tmp = tmp * 2 - z
# print(res)


# 输出：'10101.101'
# print("{:#o}".format(10)) #八进制
# print("{:#x}".format(10)) #十六进制

#print("{:e}".format(31415.5678)) #科学计数法

"""输出百分数"""
# print("{:.2%}".format(0.25))



"""f-string""" #使用最简单
# print(f"{1+2} love {2**2} love {3**3}")
# x=3.1415926
# print(f"{x:.2f}")