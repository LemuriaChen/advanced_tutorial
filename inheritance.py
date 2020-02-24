

# Example 1

class Animal(object):

    def __init__(self, name='a', age=13):
        self.name = name
        self.age = age

    def eat(self):
        print("Animal " + self.name + " is eating foods")

    def sleep(self):
        print("Animal " + self.name + " is sleeping")


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def bark(self):
        print("Dog " + self.name + " is barking, it is " + self.color)

    def eat(self):
        print("Dog " + self.name + " is eating foods")


my_dog = Dog('msh', 18, 'red')
my_dog.bark()
my_dog.eat()
my_dog.sleep()


# super
# super() 函数是用于调用父类(超类)的一个方法。
# super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题
# 但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。


# Example 2

class Base:
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        super().__init__()
        print('A.__init__')


class B(Base):
    def __init__(self):
        super().__init__()
        print('B.__init__')


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print('C.__init__')


print(C.__mro__)
print(C())









