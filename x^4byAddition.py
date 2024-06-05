def xTimesx(x):
    x2 = 0
    for i in range(x):
        x2 += x
    return x2

def x2Timesx2(x2):
    x4 = 0
    for i in range(x2):
        x4 += x2
    return x4

x = int(input())

x2 = xTimesx(x)
x4 = x2Timesx2(x2)

print(str(x4))