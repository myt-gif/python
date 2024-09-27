class Person:
    # 初始化方法，用于创建实例时设置属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法，用于显示个人信息
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    # 类方法，通常用于创建特殊的实例
    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous", 0)

    # 静态方法，与类的实例无关
    @staticmethod
    def is_adult(age):
        return age >= 18


# 创建一个 Person 类的实例
person1 = Person("Alice", 30)

# 调用实例方法
print(person1.greet())  # 输出: Hello, my name is Alice and I am 30 years old.

# 使用类方法创建一个实例
person2 = Person.create_anonymous()
print(person2.greet())  # 输出: Hello, my name is Anonymous and I am 0 years old.

# 调用静态方法
print(Person.is_adult(20))  # 输出: True
