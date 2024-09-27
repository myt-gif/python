import decimal
"""Python 中的 decimal 模块提供了 Decimal 类，
用于高精度的浮点数运算。与内建的 float 类型相比，
Decimal 提供了更高的精度和更可靠的舍入控制，
尤其在金融和科学计算中非常有用。通过使用 Decimal 类，
可以避免浮点数运算中的常见精度问题。"""


#整数 浮点数 复数(整数很专业 浮点数有些误差) 使用decimal来解决误差问题

#python很合适做大数运算 无范围限制
#print(123456789123/123)

"""#解决浮点数精度问题"""
# a=decimal.Decimal('0.1')
# b=decimal.Decimal('0.2')
# print(a+b)
# c=decimal.Decimal('0.3')
# print(a+b==c)

""" #E计法(科学计数法)"""
# print(0.00005) #5e-05 即5*(10^-5)

""" #复数"""
# print(1+2j) #1是实部 2是虚部 都是以浮点数的形式存放的
# x=1+2j
# print(x.real) #获取实部
# print(x.imag) #获取虚部

"""数字之间的运算 #公式 x相当于(x//y)*y+(x%y) x除数 y被除数"""
# print(3/2)
# print(3//2)#地板除 取比目标结果小的最大整数
# print(-3//2)

# print(3%2)
# print(divmod(3,2))
# print(6%2)

# print(abs(-520))
# print(abs(-3.14))
# print(abs(1+2j)) #返回复数的模

# print(int(9.99)) #int()直接把小数部分拿掉
# print(float(520))
# print(float("3.14"))
# print(complex("1+2j"))

# print(pow(2,3,5)) #结果为2的3次幂再对5取余