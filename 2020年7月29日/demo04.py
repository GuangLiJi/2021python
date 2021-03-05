
def power1(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power1(5, 3))