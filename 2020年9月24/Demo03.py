age = 18
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
print('=================')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)
print('=================')
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
print('=================')
print(abs(-1000.10))
print('=================')
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
print("----------------------------------")
def power(x):
    return x * x
print(power(15))
# 如果我们要计算x3怎么办？可以再定义一个power3函数，但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
print("------------------")