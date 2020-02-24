
import time


# Example 1
# 下面这段代码，实际上是用deco函数在给run函数加一个计时器的功能，而任何包含了@deco的函数，都会有这样的功能
# 这样做的好处主要有：
# 1）每个需要记时的函数，只需要@deco就可以了，这样可以节省很多代码量，
# 2）在不改变run1，run2代码的基础上，就能实现给两个函数加功能

def deco(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'{round(end - start, 4)} seconds used.')
    return wrapper


@deco
def run1():
    for i in range(100):
        if i % 10 == 0:
            print(i)


@deco
def run2():
    time.sleep(2)


run1()
run2()

"""
这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数。
其中作为参数的这个函数func()就在返回函数wrapper()的内部执行。然后在函数func()前面加上@deco，
func()函数就相当于被注入了计时功能，现在只要调用func()，它就已经变身为“新的功能更多”的函数了。
所以这里装饰器就像一个注入符号：有了它，拓展了原来函数的功能既不需要侵入函数内更改代码，也不需要重复执行原函数。
"""


# Example 2
# 装饰器带有参数，这些参数其实就是我想要加功能的函数的参数，这里的wrapper其实可以看作是函数的抽象类

def deco(func):
    def wrapper(a, b):
        start = time.time()
        func(a, b)
        end = time.time()
        print(f'{round(end - start, 4)} seconds used.')
    return wrapper


@deco
def add(a, b):
    print(a + b)


@deco
def mul(a, b):
    print(a * b)


add(3, 4)
mul(3, 4)


# Example 3
# 装饰器带有不定个数的参数

def deco(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'{round(end - start, 4)} seconds used.')
    return wrapper


@deco
def add1(a, b):
    print(a + b)


@deco
def add2(a, b, c):
    print(a + b + c)


add1(3, 4)
add2(3, 4, 5)


# Example 4
# 多个装饰器
# 多个装饰器执行的顺序就是从最后一个装饰器开始，执行到第一个装饰器，再执行函数本身。

def deco1(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('this is deco1.')
        func(*args, **kwargs)
        end = time.time()
        print(f'{round(end - start, 4)} seconds used.')
        print('deco1 end.')
    return wrapper


def deco2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print('this is deco2.')
        func(*args, **kwargs)
        end = time.time()
        print(f'{round(end - start, 4)} seconds used.')
        print('deco2 end.')
    return wrapper


@deco1
@deco2
def add(a, b):
    print(a+b)


add(3, 4)
