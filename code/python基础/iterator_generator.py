'''迭代器iterator：用来访问可迭代对象的工具,迭代器it = iter(obj)函数返回的对象(实例),迭代器可以用next(it)函数获取可迭代对象的数据'''
# 迭代器函数
# iter(iterable)从可迭代对象中返回一个迭代器；
# iterable必须是能提供一个迭代器的对象
# next(iterable)从迭代器获取下一个记录，如果无法获取下一条记录(获取完数据后)，则出发stopiterator异常；迭代器只能往前取值，不会后退
lst = [1,2,4,5,7]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
# 1
# 2
# 4
# 5
# 7
# StopIteration


# 生成器generator：生成可迭代对象,分为两种生成器函数和生成器表达式
def mygenerator():
    '''生成器函数
    动态生成数据'''
    print('准备生成数据')
    yield 1
    yield 3
    yield 4
    yield 6

# 返回一个生成器
gen = mygenerator()
# 获取迭代器
it = iter(gen)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# for循环遍历
for x in mygenerator():
    print(x)


# 生成器表达式
gen = (x**2 for x in range(1,5))
it = iter(gen)
print(next(it))
