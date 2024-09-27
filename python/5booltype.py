#False True

"""
  定义为False的对象:None False
  值为0的数字类型:0 0.0 0j Decimal(0) Fraction(0,1)->表示的是分子为0 分母为1的有理数
  空的序列和集合:'' () [] {} set() range(0)
"""
print(bool(520)) #对于数字 只有0才是false
print(bool("假")) #对于字符串 只有空字符串是false
print(bool("false"))
print(False) 
